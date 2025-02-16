from typing import List

from polars import Expr, lit


def create_columns(statistics: dict[str, int]) -> List[Expr]:
    return [lit(statistics[key]).alias(key) for key in statistics.keys()]
