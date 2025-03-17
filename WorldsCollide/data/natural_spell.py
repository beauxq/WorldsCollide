from collections.abc import Sequence


class NaturalSpell:
    def __init__(self, id: int, data: Sequence[int]) -> None:
        self.id = id

        self.spell = data[0]
        self.level = data[1]

    def data(self) -> list[int]:
        from ..data.natural_magic import NaturalMagic
        data = [0x00] * NaturalMagic.SPELL_DATA_SIZE

        data[0] = self.spell
        data[1] = self.level

        return data

    def print(self) -> None:
        print(f"{self.id}: {self.spell} {self.level}")
