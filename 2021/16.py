"""Day 16: Packet Decoder."""

from math import prod
from aoc.puzzle import Puzzle


class Packet:
    def __init__(self, bits):
        self.bits = bits
        self.version = int(self.bits[0:3], 2)
        self.id = int(self.bits[3:6], 2)
        self.content = self.decode_value() if self.id == 4 else self.decode_operator()

    def decode_value(self):
        """Decode binary values. Packet's size is calculated for
        operator's sub-packets identification.
        """
        value = ""
        k = 6
        while True:
            group = self.bits[k : k + 5]
            value += group[1:]
            k += 5
            if group[0] == "0":
                self.size = k
                break
        return int(value, 2)

    def decode_operator(self):
        """Separate packets included in an operator.

        All bits of the content are decoded as a single packet. Its
        size is then used to identify remaining bits to decode.
        The process is repeated until:
            - there is no bits left (lenght_id == "0")
            - we got the correct amount of packets (length_id == "1")
        """
        length_id = self.bits[6]
        content = []
        if length_id == "0":
            self.size = 22 + int(self.bits[7:22], 2)
            remaining_bits = self.bits[22 : self.size]
            while remaining_bits:
                content.append(Packet(remaining_bits))
                remaining_bits = remaining_bits[content[-1].size :]
        else:
            sub_count = int(self.bits[7:18], 2)
            remaining_bits = self.bits[18:]
            for _ in range(sub_count):
                content.append(Packet(remaining_bits))
                remaining_bits = remaining_bits[content[-1].size :]
            self.size = 18 + sum(packet.size for packet in content)
        return content

    def versions_sum(self):
        if self.id == 4:
            return self.version
        else:
            return self.version + sum(p.versions_sum() for p in self.content)

    @property
    def value(self):
        if self.id == 4:
            return self.content
        elif self.id == 0:
            return sum(packet.value for packet in self.content)
        elif self.id == 1:
            return prod(packet.value for packet in self.content)
        elif self.id == 2:
            return min(packet.value for packet in self.content)
        elif self.id == 3:
            return max(packet.value for packet in self.content)
        elif self.id == 5:
            return 1 if self.content[0].value > self.content[1].value else 0
        elif self.id == 6:
            return 1 if self.content[0].value < self.content[1].value else 0
        elif self.id == 7:
            return 1 if self.content[0].value == self.content[1].value else 0


class Today(Puzzle):
    def parser(self):
        self.bits = "".join(f"{int(f'0x{x}', 16):04b}" for x in self.input)

    def part_one(self):
        self.transmission = Packet(self.bits)
        return self.transmission.versions_sum()

    def part_two(self):
        return self.transmission.value


solutions = (977, 101501020883)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
