from collections.abc import Sequence


class CharacterSprite:
    def __init__(self, id: int, data: Sequence[int]) -> None:
        self.id = id
        self._data = data

    @property
    def data(self) -> Sequence[int]:
        return self._data

    @data.setter
    def data(self, new_data: Sequence[int]) -> None:
        self._data = new_data
