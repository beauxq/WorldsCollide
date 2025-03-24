from typing import TypeVar

from ..constants.objectives.results import names as possible_result_names

T = TypeVar("T")


class ResultDict(dict[str, T]):
    """
    when testing if a dictionary of results contains a key
    assert that the result name is possible (e.g. not misspelled/changed/removed)
    """

    def __contains__(self, item: object) -> bool:
        assert item in possible_result_names
        return super().__contains__(item)
