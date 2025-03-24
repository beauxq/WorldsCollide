# flatten values into list
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def flatten(values: T | Sequence[T | Sequence[T]]) -> list[T]:
    return ([y for x in values for y in flatten(x)]
            if isinstance(values, (list, tuple, bytes))
            else [values])
