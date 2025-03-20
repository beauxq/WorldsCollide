from collections.abc import Container, Sequence
from typing import TypeVar

T = TypeVar("T")


def intersection(lst1: Sequence[T], lst2: Container[T]) -> list[T]:
    """ find the intersection of two lists """
    # ref: https://www.geeksforgeeks.org/python-intersection-two-lists/#
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
