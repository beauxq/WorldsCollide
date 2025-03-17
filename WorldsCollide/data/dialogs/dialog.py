from collections.abc import Sequence

from ...data.text import get_bytes, get_string, TextType

class Dialog:
    def __init__(self, id: int, type: TextType, data: Sequence[int]) -> None:
        self.id = id
        self.type = type
        self._text = get_string(data, self.type)

        self.modified = False
        self.original_data = data

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self.modified = True
        self._text = value

    def data(self) -> Sequence[int]:
        if self.modified:
            # only convert modified text
            # converting every dialog frees up a lot of space (~7-10k bytes) but is slightly slower
            # remove modified flag and convert all if extra dialog space needed
            return get_bytes(self.text, self.type)
        return self.original_data

    def __str__(self) -> str:
        return f"{self.id:<4} '{self.text}'"

    def print(self) -> None:
        print(str(self))
