"""--- Day 9: Disk Fragmenter ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.disk = list(map(int, self.input))

    def part_one(self):
        """Files are stored in a list with the ids as indexes and the
        sizes as values. Iterating through the disk, blocks are taken
        from the lowest ids for even spaces and from the highest for
        odd ones.
        """
        files = self.disk[::2]
        left_id, right_id = 0, len(files) - 1
        checksum, block = 0, 0
        for k, size in enumerate(self.disk):
            if not k % 2:
                for _ in range(size):
                    checksum += block * left_id
                    files[left_id] -= 1
                    block += 1
                    if not files[left_id]:
                        left_id += 1
                        if not files[left_id]:
                            return checksum
            else:
                for _ in range(size):
                    checksum += block * right_id
                    files[right_id] -= 1
                    block += 1
                    if not files[right_id]:
                        right_id -= 1
                        if not files[right_id]:
                            return checksum

    def part_two(self):
        """Files are still stored in a list with the ids as indexes,
        but the value is now storing their size, previous id, next id
        and the available space after it. For first and last files,
        previous and next ids are set to -1.
        Reordering files is simply done by replacing the previous and
        next ids and removing the spaces.
        """
        # Prepare disk
        disk, fid = [], 0
        for k, size in enumerate(self.disk):
            if not k % 2:
                disk.append([size, fid - 1, fid + 1, 0])
                fid += 1
            else:
                disk[-1][-1] = size
        disk[-1][2] = -1

        for fid in reversed(range(len(disk))):
            f = disk[fid]
            pointer = 0
            while pointer != fid:
                p = disk[pointer]
                if p[3] >= f[0]:
                    break
                pointer = p[2]
            else:
                continue

            # Move free space around
            disk[f[1]][3] += f[0] + f[3]
            f[3] = p[3] - f[0]
            p[3] = 0
            # Update previous and next ids
            a, b = f[1], f[2]
            disk[a][2] = b
            disk[b][1] = a
            f[1], f[2] = pointer, p[2]
            p[2], disk[f[2]][1] = fid, fid

        block, pointer, checksum = 0, 0, 0
        while pointer != -1:
            f = disk[pointer]
            for _ in range(f[0]):
                checksum += pointer * block
                block += 1
            block += f[3]
            pointer = f[2]
        return checksum


if __name__ == "__main__":
    Today().solve()
