class Control:
    def __init__(self, id: int, attack_data: list):
        self.id = id

        self.attack_data_array = attack_data

    def attack_data(self):
        from ..data.controls import Controls
        data = [0x00] * Controls.ATTACKS_DATA_SIZE

        data = self.attack_data_array

        return data

    def print(self):
        attack_str = ""
        for attack in self.attack_data:
            attack_str += f"{attack} "

        print(f"{self.id} {attack_str}")
