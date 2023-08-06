import enum
import hashlib
import operator
from dataclasses import dataclass
from datetime import datetime
from functools import reduce
from typing import Any, Callable, List, Optional, Tuple, Union, Dict

import pyspark.sql.functions as F
import pyspark.sql.types as T
from pyspark.sql import DataFrame, Observation, SparkSession, Column, Row
from toolz import compose, valfilter  # type: ignore
from itertools import chain
from . import dataframe as D

import logging

logger = logging.getLogger(__name__)


class CheckLevel(enum.Enum):
    WARNING = 0
    ERROR = 1


class CheckDataType(enum.Enum):
    AGNOSTIC = 0
    NUMERIC = 1
    STRING = 2
    DATE = 3
    TIMESTAMP = 4


@dataclass(frozen=True)
class Rule:
    method: str
    column: Union[Tuple, str]
    value: Optional[Any]
    data_type: CheckDataType
    coverage: float = 1.0

    def __repr__(self):
        return f"Rule(method:{self.method}, column:{self.column}, value:{self.value}, data_type:{self.data_type}, coverage:{self.coverage}"


@dataclass(frozen=True)
class ComputeInstruction:
    rule: Rule
    expression: Union[Column, Callable]
    predicate: Union[Column, Callable, None] = None


class Check:
    def __init__(
        self,
        level: Union[CheckLevel, int],
        name: str,
        execution_date: datetime = datetime.today(),
    ):
        self._compute: Dict[str, ComputeInstruction] = {}
        self._unique: Dict[str, ComputeInstruction] = {}
        self._union: Dict[str, ComputeInstruction] = {}
        if isinstance(level, int):
            level = CheckLevel(level)

        self.level = level
        self.name = name
        self.date = execution_date
        self.rows = -1

    def __repr__(self):
        return f"Check(level:{self.level}, desc:{self.name}, rules:{self.sum})"

    @property
    def sum(self):
        """Collect compute, unique and union type of rules"""
        return len(self._integrate_compute().keys())

    @property
    def rules(self):
        """Returns all rules defined for check"""
        return list(map(lambda x: x.rule, self._integrate_compute().values()))

    @property
    def expressions(self):
        """Returns all summary expressions for validation"""
        return list(map(lambda x: x.expression, self._integrate_compute().values()))

    @property
    def predicates(self):
        """Returns all filtering predicates for negative samples"""
        return list(
            filter(
                lambda x: x is not None,
                map(lambda x: x.predicate, self._integrate_compute().values()),
            )
        )

    def _generate_rule_key_id(
        self,
        method: str,
        column: Union[Tuple, str],
        value: Any,
        coverage: float,
    ):
        """A hash function to generate unique identifiers for rules"""
        return hashlib.blake2s(
            bytes(f"{method}{column}{value}{coverage}", "utf-8")
        ).hexdigest()

    def _generate_rule_hash(self, rule: Rule):
        """A hash funtion for unique rule identifiers"""
        return self._generate_rule_key_id(
            rule.method, rule.column, rule.value, rule.coverage
        )

    def _single_value_rule(
        self,
        column: str,
        value: Optional[Any],
        operator: Callable,
    ):
        return F.sum((operator(F.col(column), value)).cast("integer"))

    def _integrate_compute(self) -> Dict:
        """Unifies the compute dictionaries from observation and select forms"""
        return {**self._compute, **self._unique, **self._union}

    @staticmethod
    def _compute_columns(columns: Union[str, List[str]]) -> List[str]:
        """Confirm that all compute columns exists in dataframe"""

        def _normalize_columns(col: Union[str, List[str]], agg: List[str]) -> List[str]:
            """Recursive consilidation of compute columns"""
            if isinstance(col, str):
                agg.append(col)
            else:
                [_normalize_columns(inner_col, agg) for inner_col in col]
            return agg

        return _normalize_columns(columns, [])

    def is_complete(self, column: str, pct: float = 1.0):
        """Validation for non-null values in column"""
        rule = Rule("is_complete", column, "N/A", CheckDataType.AGNOSTIC, pct)
        predicate = F.col(f"`{column}`").isNull()
        expression = F.sum(F.col(f"`{column}`").isNotNull().cast("integer"))
        key = self._generate_rule_hash(rule)
        self._compute[key] = ComputeInstruction(
            rule,
            expression,
            predicate,
        )

        return self

    def are_complete(self, column: str, pct: float = 1.0):
        """Validation for non-null values in a group of columns"""
        # if isinstance(column, List):
        #    column = tuple(column)
        key = self._generate_rule_key_id("are_complete", column, "N/A", pct)
        self._compute[key] = ComputeInstruction(
            Rule("are_complete", column, "N/A", CheckDataType.AGNOSTIC, pct),
            reduce(
                operator.add,
                [F.sum(F.col(f"`{c}`").isNotNull().cast("integer")) for c in column],
            )
            / len(column),
        )
        return self

    def is_unique(self, column: str, pct: float = 1.0):
        """Validation for unique values in column"""
        key = self._generate_rule_key_id("is_unique", column, "N/A", pct)
        self._unique[key] = ComputeInstruction(
            Rule("is_unique", column, "N/A", CheckDataType.AGNOSTIC, pct),
            F.count_distinct(F.col(column)),
        )
        return self

    def are_unique(self, column: Tuple[str], pct: float = 1.0):
        """Validation for unique values in a group of columns"""
        if isinstance(column, List):
            column = tuple(column)
        key = self._generate_rule_key_id("are_unique", column, "N/A", pct)
        self._unique[key] = ComputeInstruction(
            Rule("are_unique", column, "N/A", CheckDataType.AGNOSTIC, pct),
            F.count_distinct(*[F.col(c) for c in column]),
        )
        return self

    def is_greater_than(self, column: str, value: float, pct: float = 1.0):
        """Validation for numeric greater than value"""
        key = self._generate_rule_key_id("is_greater_than", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_greater_than", column, value, CheckDataType.NUMERIC, pct),
            self._single_value_rule(column, value, operator.gt),
        )
        return self

    def is_greater_or_equal_than(self, column: str, value: float, pct: float = 1.0):
        """Validation for numeric greater or equal than value"""
        key = self._generate_rule_key_id("is_greater_or_equal_than", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_greater_or_equal_than", column, value, CheckDataType.NUMERIC, pct),
            self._single_value_rule(column, value, operator.ge),
        )
        return self

    def is_less_than(self, column: str, value: float, pct: float = 1.0):
        """Validation for numeric less than value"""
        key = self._generate_rule_key_id("is_less_than", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_less_than", column, value, CheckDataType.NUMERIC, pct),
            self._single_value_rule(column, value, operator.lt),
        )
        return self

    def is_less_or_equal_than(self, column: str, value: float, pct: float = 1.0):
        """Validation for numeric less or equal than value"""
        key = self._generate_rule_key_id("is_less_or_equal_than", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_less_or_equal_than", column, value, CheckDataType.NUMERIC, pct),
            self._single_value_rule(column, value, operator.le),
        )
        return self

    def is_equal_than(self, column: str, value: float, pct: float = 1.0):
        """Validation for numeric column equal than value"""
        key = self._generate_rule_key_id("is_equal", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_equal", column, value, CheckDataType.NUMERIC, pct),
            self._single_value_rule(column, value, operator.eq),
        )
        return self

    def has_pattern(self, column: str, value: str, pct: float = 1.0):
        """Validation for string type column matching regex expression"""
        key = self._generate_rule_key_id("has_pattern", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("has_pattern", column, value, CheckDataType.STRING, pct),
            F.sum((F.length(F.regexp_extract(column, value, 0)) > 0).cast("integer")),
        )
        return self

    def has_min(self, column: str, value: float, pct: float = 1.0):
        """Validation of a column’s minimum value"""
        key = self._generate_rule_key_id("has_min", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("has_min", column, value, CheckDataType.NUMERIC),
            F.min(F.col(column)) == value,
        )
        return self

    def has_max(self, column: str, value: float, pct: float = 1.0):
        """Validation of a column’s maximum value"""
        key = self._generate_rule_key_id("has_max", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("has_max", column, value, CheckDataType.NUMERIC),
            F.max(F.col(column)) == value,
        )
        return self

    def has_std(self, column: str, value: float, pct: float = 1.0):
        """Validation of a column’s standard deviation"""
        key = self._generate_rule_key_id("has_std", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("has_std", column, value, CheckDataType.NUMERIC),
            F.stddev_pop(F.col(column)) == value,
        )
        return self

    def has_mean(self, column: str, value: float, pct: float = 1.0):
        """Validation of a column's average/mean"""
        key = self._generate_rule_key_id("has_mean", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("has_mean", column, value, CheckDataType.NUMERIC),
            F.mean(F.col(f"`{column}`")).eqNullSafe(value),
        )
        return self

    def is_between(self, column: str, value: Tuple[Any], pct: float = 1.0):
        """Validation of a column between a range"""

        # Create tuple if user pass list
        if isinstance(value, List):
            value = tuple(value)

        key = self._generate_rule_key_id("is_between", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_between", column, value, CheckDataType.AGNOSTIC, pct),
            F.sum(F.col(column).between(*value).cast("integer")),  # type: ignore
        )
        return self

    def is_contained_in(
        self, column: str, value: Tuple[str, int, float], pct: float = 1.0
    ):
        """Validation of column value in set of given values"""
        # Create tuple if user pass list
        if isinstance(value, List):
            value = tuple(value)

        # Check value type to later assess correct column type
        if [isinstance(v, str) for v in value]:
            check = CheckDataType.STRING
        else:
            check = CheckDataType.NUMERIC

        key = self._generate_rule_key_id("is_contained_in", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_contained_in", column, value, check),
            F.sum((F.col(column).isin(list(value))).cast(T.LongType())),
        )
        return self

    def is_in(self, column: str, value: Tuple[str, int, float], pct: float = 1.0):
        """Vaidation of column value in set of given values"""
        return self.is_contained_in(column, value, pct)

    def is_on_weekday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is in a Mon-Fri time range"""
        key = self._generate_rule_key_id("is_on_weekday", column, "Mon-Fri", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_weekday", column, "Mon-Fri", CheckDataType.DATE, pct),
            F.sum(F.dayofweek(f"`{column}`").between(2, 6).cast("integer")),
        )
        return self

    def is_on_weekend(self, column: str, pct: float = 1.0):
        """Validates a datetime column is in a Sat-Sun time range"""
        key = self._generate_rule_key_id("is_on_weekend", column, "Sat-Sun", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_weekend", column, "Sat-Sun", CheckDataType.DATE, pct),
            F.sum(F.dayofweek(f"`{column}`").isin([1, 7]).cast("integer")),
        )
        return self

    def is_on_monday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Mon"""
        key = self._generate_rule_key_id("is_on_monday", column, "Mon", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_monday", column, "Mon", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 2).cast("integer")),
        )
        return self

    def is_on_tuesday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Tue"""
        key = self._generate_rule_key_id("is_on_tuesday", column, "Tue", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_tuesday", column, "Tue", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 3).cast("integer")),
        )
        return self

    def is_on_wednesday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Wed"""
        key = self._generate_rule_key_id("is_on_wednesday", column, "Wed", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_wednesday", column, "Wed", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 3).cast("integer")),
        )
        return self

    def is_on_thursday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Thu"""
        key = self._generate_rule_key_id("is_on_thursday", column, "Thu", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_thursday", column, "Thu", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 4).cast("integer")),
        )
        return self

    def is_on_friday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Fri"""
        key = self._generate_rule_key_id("is_on_friday", column, "Fri", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_friday", column, "Fri", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 5).cast("integer")),
        )
        return self

    def is_on_saturday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Sat"""
        key = self._generate_rule_key_id("is_on_saturday", column, "Sat", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_saturday", column, "Sat", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 7).cast("integer")),
        )
        return self

    def is_on_sunday(self, column: str, pct: float = 1.0):
        """Validates a datetime column is on Sun"""
        key = self._generate_rule_key_id("is_on_sunday", column, "Sun", pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_sunday", column, "Sun", CheckDataType.DATE, pct),
            F.sum((F.dayofweek(f"`{column}`") == 1).cast("integer")),
        )
        return self

    def is_on_schedule(self, column: str, value: Tuple[Any], pct: float = 1.0):
        """Validation of a datetime column between an hour interval"""

        # Create tuple if user pass list
        if isinstance(value, List):
            value = tuple(value)

        key = self._generate_rule_key_id("is_on_schedule", column, value, pct)
        self._compute[key] = ComputeInstruction(
            Rule("is_on_schedule", column, value, CheckDataType.TIMESTAMP, pct),
            F.sum(F.hour(column).between(*value).cast("integer")),  # type: ignore
        )
        return self

    def has_percentile(
        self,
        column: str,
        value: float,
        percentile: float,
        precision: int = 10000,
        pct: float = 1.0,
    ):
        """Validation of a column percentile value"""
        key = self._generate_rule_key_id(
            "has_percentile", column, (value, percentile, precision), pct
        )
        self._unique[key] = ComputeInstruction(
            Rule(
                "has_percentile",
                column,
                (value, percentile, precision),
                CheckDataType.NUMERIC,
                pct,
            ),
            F.percentile_approx(
                F.col(f"`{column}`").cast(T.DoubleType()), percentile, precision
            ).eqNullSafe(value),
        )
        return self

    def has_max_by(
        self, column_source: str, column_target: str, value: float, pct: float = 1.0
    ):
        """Validation of a column maximum based on other column maximum"""
        key = self._generate_rule_key_id(
            "has_max_by", (column_source, column_target), value, pct
        )
        self._compute[key] = ComputeInstruction(
            Rule(
                "has_max_by",
                (column_source, column_target),
                value,
                CheckDataType.NUMERIC,
            ),
            F.max_by(column_target, column_source) == value,
        )
        return self

    def has_min_by(
        self, column_source: str, column_target: str, value: float, pct: float = 1.0
    ):
        """Validation of a column minimum based on other column minimum"""
        key = self._generate_rule_key_id(
            "has_min_by", (column_source, column_target), value, pct
        )
        self._compute[key] = ComputeInstruction(
            Rule(
                "has_min_by",
                (column_source, column_target),
                value,
                CheckDataType.NUMERIC,
            ),
            F.min_by(column_target, column_source) == value,
        )
        return self

    def has_correlation(
        self, column_left: str, column_right: str, value: float, pct: float = 1.0
    ):
        """Validates the correlation between 2 columns with some tolerance"""

        key = self._generate_rule_key_id(
            "has_correlation", (column_left, column_right), value, pct
        )
        self._unique[key] = ComputeInstruction(
            Rule(
                "has_correlation",
                (column_left, column_right),
                value,
                CheckDataType.NUMERIC,
            ),
            F.corr(
                F.col(f"`{column_left}`").cast(T.DoubleType()),
                F.col(f"`{column_right}`").cast(T.DoubleType()),
            ).eqNullSafe(F.lit(value)),
        )
        return self

    def satisfies(self, predicate: str, column: str, pct: float = 1.0):
        """Validation of a column satisfying a SQL-like predicate"""
        key = self._generate_rule_key_id("satisfies", column, predicate, pct)
        self._compute[key] = ComputeInstruction(
            Rule("satisfies", column, predicate, CheckDataType.AGNOSTIC, pct),
            F.sum(F.expr(predicate).cast("integer")),
        )
        return self

    def has_entropy(self, column: str, value: float, tolerance: float = 0.01):
        """Validation for entropy calculation on continuous values"""
        key = self._generate_rule_key_id("has_entropy", column, value, tolerance)

        def _execute(dataframe: DataFrame):
            return (
                dataframe.groupby(column)
                .count()
                .select(F.collect_list("count").alias("freq"))
                .select(
                    F.col("freq"),
                    F.aggregate("freq", F.lit(0.0), lambda a, b: a + b).alias("rows"),
                )
                .withColumn("probs", F.transform("freq", lambda x: x / F.col("rows")))
                .withColumn("n_labels", F.size("probs"))
                .withColumn("log_labels", F.log("n_labels"))
                .withColumn("log_prob", F.transform("probs", lambda x: F.log(x)))
                .withColumn(
                    "log_classes",
                    F.transform("probs", lambda x: F.log((x / x) * F.col("n_labels"))),
                )
                .withColumn("entropy_vals", F.arrays_zip("probs", "log_prob"))
                .withColumn(
                    "product_prob",
                    F.transform(
                        "entropy_vals",
                        lambda x: x.getItem("probs") * x.getItem("log_prob"),
                    ),
                )
                .select(
                    (
                        F.aggregate(
                            "product_prob", F.lit(0.0), lambda acc, x: acc + x
                        ).alias("p")
                        / F.col("log_labels")
                        * -1
                    ).alias("entropy")
                )
                .select(
                    F.expr(
                        f"entropy BETWEEN {value-tolerance} AND {value+tolerance}"
                    ).alias(key)
                )
            )

        self._union[key] = ComputeInstruction(
            Rule("has_entropy", column, value, CheckDataType.AGNOSTIC), _execute
        )

        return self

    def has_weekday_continuity(self, column: str, pct: float = 1.0):
        """Validates that there is no missing dates using only week days in the date/timestamp column"""
        key = self._generate_rule_key_id(
            "has_weekday_continuity", column, "⊂{Mon-Fri}", pct
        )

        def _execute(dataframe: DataFrame):
            _weekdays = lambda x: x.filter(F.dayofweek(column).isin([2, 3, 4, 5, 6]))
            _date_only = lambda x: x.select(F.to_date(column).alias(column))
            full_interval = (
                dataframe.select(
                    F.explode(
                        F.sequence(
                            F.min(column), F.max(column), F.expr("interval 1 day")
                        )
                    ).alias(column)
                )
                .transform(_weekdays)
                .transform(_date_only)
            )
            return full_interval.join(
                dataframe.transform(_date_only), column, how="left_anti"
            ).select(
                (F.expr(f"{dataframe.count()} - count(distinct({column}))")).alias(key)
            )

        self._union[key] = ComputeInstruction(
            Rule(
                "has_weekday_continuity", column, "⊂{Mon-Fri}", CheckDataType.DATE, pct
            ),
            _execute,
        )

        return self

    def validate(self, spark: SparkSession, dataframe: DataFrame, metadata: dict = {}):
        """Compute all rules in this check for specific data frame"""

        # Merge `unique` and `compute` dict
        unified_rules = self._integrate_compute()
        rule_expressions = unified_rules.values()
        # Check the dictionnary is not empty
        assert (
            unified_rules
        ), "Check is empty. Add validations i.e. is_complete, is_unique, etc."

        # Check dataframe is spark dataframe
        assert isinstance(
            dataframe, DataFrame
        ), "Cualle operates only with Spark Dataframes"

        # Pre-validate column names
        _col = compose(operator.attrgetter("column"), operator.attrgetter("rule"))
        column_set = set(Check._compute_columns(list(map(_col, rule_expressions))))
        unknown_columns = column_set.difference(set(dataframe.columns))
        assert not unknown_columns, f"Column(s): {unknown_columns} not in dataframe"

        # Pre-Validation of numeric data types

        _numeric = lambda x: x.rule.data_type == CheckDataType.NUMERIC
        _date = lambda x: x.rule.data_type == CheckDataType.DATE
        _timestamp = lambda x: x.rule.data_type == CheckDataType.TIMESTAMP
        _string = lambda x: x.rule.data_type == CheckDataType.STRING
        assert set(
            Check._compute_columns(
                map(_col, valfilter(_numeric, unified_rules).values())  # type: ignore
            )
        ).issubset(D.numeric_fields(dataframe))
        assert set(
            Check._compute_columns(
                map(_col, valfilter(_string, unified_rules).values())  # type: ignore
            )
        ).issubset(D.string_fields(dataframe))
        assert set(
            Check._compute_columns(map(_col, valfilter(_date, unified_rules).values()))  # type: ignore
        ).issubset(D.date_fields(dataframe))
        assert set(
            Check._compute_columns(
                map(_col, valfilter(_timestamp, unified_rules).values())  # type: ignore
            )
        ).issubset(D.timestamp_fields(dataframe))

        if self._compute:
            observation = Observation(self.name)
            for k, v in self._compute.items():
                logger.info(str(v.expression))

            df_observation = dataframe.observe(
                observation,
                *[
                    compute_instruction.expression.alias(hash_key)  # type: ignore
                    for hash_key, compute_instruction in self._compute.items()
                ],
            )
            rows = df_observation.count()
            observation_result = observation.get
            logger.info(observation_result)
        else:
            observation_result = {}
            rows = dataframe.count()

        self.rows = rows

        unique_observe = (
            dataframe.select(
                *[
                    compute_instrunction.expression.alias(hash_key)  # type: ignore
                    for hash_key, compute_instrunction in self._unique.items()
                ]
            )
            .first()
            .asDict()  # type: ignore
        )

        union_observe = {
            k: operator.attrgetter(k)(compute_instruction.expression(dataframe).first())  # type: ignore
            for k, compute_instruction in self._union.items()
        }

        unified_results = {**unique_observe, **observation_result, **union_observe}

        _calculate_pass_rate = lambda observed_column: (
            F.when(observed_column == "false", F.lit(0.0))
            .when(observed_column == "true", F.lit(1.0))
            .otherwise(observed_column.cast(T.DoubleType()) / self.rows)  # type: ignore
        )
        _evaluate_status = lambda pass_rate, pass_threshold: (
            F.when(pass_rate >= pass_threshold, F.lit("PASS")).otherwise(F.lit("FAIL"))
        )
        _metadata = F.create_map(
            *chain.from_iterable([(F.lit(k), F.lit(v)) for k, v in metadata.items()])
        )
        return (
            spark.createDataFrame(
                [
                    Row(  # type: ignore
                        index,
                        compute_instruction.rule.method,
                        str(compute_instruction.rule.column),
                        str(compute_instruction.rule.value),
                        unified_results[hash_key],
                        compute_instruction.rule.coverage,
                    )
                    for index, (hash_key, compute_instruction) in enumerate(
                        unified_rules.items(), 1
                    )
                ],
                schema="id int, rule string, column string, value string, result string, pass_threshold string",
            )
            .select(
                F.col("id"),
                F.lit(self.date.strftime("%Y-%m-%d %H:%M:%S")).alias("timestamp"),
                F.lit(self.name).alias("check"),
                F.lit(self.level.name).alias("level"),
                F.col("column"),
                F.col("rule"),
                F.col("value"),
                F.lit(rows).alias("rows"),
                (rows - F.col("result").cast("long")).alias("violations"),
                _calculate_pass_rate(F.col("result")).alias("pass_rate"),
                F.col("pass_threshold").cast(T.DoubleType()),
                F.lit(_metadata).alias("metadata"),
            )
            .withColumn(
                "status",
                _evaluate_status(F.col("pass_rate"), F.col("pass_threshold")),
            )
        )

    def samples(self, dataframe: DataFrame, rule_index: int = None) -> DataFrame:
        if not rule_index:
            return reduce(
                DataFrame.unionAll,
                [dataframe.filter(predicate) for predicate in self.predicates],
            ).drop_duplicates()
        elif isinstance(rule_index, int):
            return reduce(
                DataFrame.unionAll,
                [
                    dataframe.filter(predicate)
                    for index, predicate in enumerate(self.predicates, 1)
                    if rule_index == index
                ],
            )
        elif isinstance(rule_index, list):
            return reduce(
                DataFrame.unionAll,
                [
                    dataframe.filter(predicate)
                    for index, predicate in enumerate(self.predicates, 1)
                    if index in rule_index
                ],
            ).drop_duplicates()
