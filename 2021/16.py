"""Day 16: Packet Decoder."""

from math import prod
from aoc.puzzle import Puzzle


class Packet:
    def __init__(self, binary):
        self.bin = binary
        self.version = int(self.bin[0:3], 2)
        self.id = int(self.bin[3:6], 2)
        self.content = self.decode_value() if self.id == 4 else self.decode_op()

    def decode_value(self):
        value = ""
        k = 6
        while True:
            group = self.bin[k : k + 5]
            value += group[1:]
            k += 5
            if group[0] == "0":
                break
        self.size = k
        return int(value, 2)

    def decode_op(self):
        sub_type = self.bin[6]
        content = []
        if sub_type == "0":
            self.size = 22 + int(self.bin[7:22], 2)
            to_read = self.bin[22 : self.size]
            while to_read:
                content.append(Packet(to_read))
                to_read = to_read[content[-1].size :]
        else:
            sub_count = int(self.bin[7:18], 2)
            to_read = self.bin[18:]
            for _ in range(sub_count):
                content.append(Packet(to_read))
                to_read = to_read[content[-1].size :]
            self.size = 18 + sum(packet.size for packet in content)
        return content

    @property
    def versions_sum(self):
        if self.id == 4:
            return self.version
        else:
            return self.version + sum(p.versions_sum for p in self.content)

    @property
    def value(self):
        if self.id == 0:
            return sum(packet.value for packet in self.content)
        elif self.id == 1:
            return prod(packet.value for packet in self.content)
        elif self.id == 2:
            return min(packet.value for packet in self.content)
        elif self.id == 3:
            return max(packet.value for packet in self.content)
        elif self.id == 4:
            return self.content
        elif self.id == 5:
            return 1 if self.content[0].value > self.content[1].value else 0
        elif self.id == 6:
            return 1 if self.content[0].value < self.content[1].value else 0
        elif self.id == 7:
            return 1 if self.content[0].value == self.content[1].value else 0


class Today(Puzzle):
    def parser(self):
        return "".join(f"{int(f'0x{x}', 16):04b}" for x in self.input)

    def part_one(self):
        self.transmission = Packet(self.input)
        return self.transmission.versions_sum

    def part_two(self):
        return self.transmission.value


solutions = (977, 101501020883)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
