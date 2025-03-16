from ..constants.objectives.results import names as possible_result_names

# when testing if a dictionary of results contains a key
# assert that the result name is possible (e.g. not misspelled/changed/removed)
class ResultDict(dict[str, "Unknown"]):
    def __contains__(self, item: object) -> bool:
        assert item in possible_result_names
        return super().__contains__(item)
