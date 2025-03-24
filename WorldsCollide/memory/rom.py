from collections.abc import Sequence


class ROM:
    SHORT_PTR_SIZE = 2  # short ptr (16-bit)
    LONG_PTR_SIZE = 3   # long ptr  (24-bit)

    def __init__(self, file_name: str) -> None:
        from ..valid_rom_file import valid_rom_file
        if not valid_rom_file(file_name):
            raise ValueError("Invalid ROM File")

        with open(file_name, "rb") as rom_file:
            self.data = list(rom_file.read())

        self.expand()

    def size(self) -> int:
        return len(self.data)

    def expand(self) -> None:
        expanded_size = 4 * 2 ** 20 # 4 mb
        self.data.extend([0xff] * (expanded_size - len(self.data)))

    def write(self, file_name: str) -> None:
        with open(file_name, "wb") as out_file:
            out_file.write(bytearray(self.data))

    def get_bits(self, address: int, mask: int) -> int:
        return self.data[address] & mask

    def get_byte(self, address: int) -> int:
        return self.data[address]

    def get_short(self, address: int) -> int:
        return int.from_bytes(self.get_bytes(address, 2), byteorder='little')

    def get_bytes(self, address: int, count: int) -> list[int]:
        return self.data[address : address + count]

    def get_bytes_endian_swap(self, address: int, count: int) -> list[int]:
        return self.get_bytes(address, count)[::-1]

    def set_bits(self, address: int, mask: int, value: int) -> None:
        not_mask = 0xff - mask # be careful of signed values
        self.data[address] = (value & mask) | (self.data[address] & not_mask)

    def set_bit_num(self, address: int, bit_num: int, value: bool) -> None:
        # set bit_num starting at address, e.g. bit_num = 12 address = 0xa0000, sets bit 4 in byte 0xa0001
        byte = bit_num // 8
        bit = bit_num % 8

        if value:
            self.data[address + byte] = self.data[address + byte] | (1 << bit)
        else:
            self.data[address + byte] = self.data[address + byte] & ~(1 << bit)

    def set_byte(self, address: int, value: int) -> None:
        self.data[address] = value

    def set_short(self, address: int, value: int) -> None:
        self.set_bytes(address, value.to_bytes(2, 'little'))

    def set_bytes(self, address: int, values: Sequence[int]) -> int:
        self.data[address : address + len(values)] = values
        return address + len(values)

    def set_bytes_endian_swap(self, address: int, values: Sequence[int]) -> int:
        return self.set_bytes(address, values[::-1])

    def print_byte(self, address: int, decimal: bool = False) -> None:
        if decimal:
            print(self.get_byte(address))
        else:
            print(f'0x{self.get_byte(address):02x}')

    def print_bytes(self, address: int, count: int, decimal: bool = False) -> None:
        if decimal:
            print(' '.join(str(byte) for byte in self.get_bytes(address, count)))
        else:
            print(' '.join(f"0x{byte:02x}" for byte in self.get_bytes(address, count)))

    def print_addresses(self, address: int, count: int) -> None:
        for offset, byte in enumerate(self.get_bytes(address, count)):
            print(hex(address + offset) + ": " + hex(byte))
