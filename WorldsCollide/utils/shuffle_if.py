from collections.abc import Callable, MutableSequence
from typing import TypeVar

T = TypeVar("T")


def shuffle_if(lst: MutableSequence[T], condition: Callable[[T], bool]) -> None:
    """ shuffle elements of given list that meet given condition """
    # https://stackoverflow.com/a/12238093

    indices, elements = zip(*[(i, e) for i, e in enumerate(lst) if condition(e)], strict=False)
    indices = list(indices)

    import random
    random.shuffle(indices)

    for i, e in zip(indices, elements, strict=False):
        lst[i] = e
