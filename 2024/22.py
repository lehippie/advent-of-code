"""--- Day 22: Monkey Market ---"""

from aoc.puzzle import Puzzle


def next_secret(secret):
    secret = (secret * 64) ^ secret
    secret %= 16777216
    secret = (secret // 32) ^ secret
    secret %= 16777216
    secret = (secret * 2048) ^ secret
    return secret % 16777216


class Today(Puzzle):
    def parser(self):
        self.initial_secrets = list(map(int, self.input))

    def part_one(self):
        result = 0
        for secret in self.initial_secrets:
            for _ in range(2000):
                secret = next_secret(secret)
            result += secret
        return result

    def part_two(self):
        """For each buyer, we create a dict where the key are the
        sequences of price change and the values are the prices.
        Then we search for the maximum of bananas we have for each
        sequence that appears at least once in the buyers dicts.
        """
        buyers = [{} for _ in range(len(self.initial_secrets))]
        for k, secret in enumerate(self.initial_secrets):
            price = secret % 10
            changes = []
            for _ in range(2000):
                secret = next_secret(secret)
                next_price = secret % 10
                changes.append(next_price - price)
                if len(changes) >= 4:
                    sequence = tuple(changes[-4:])
                    if sequence not in buyers[k]:
                        buyers[k][sequence] = next_price
                price = next_price

        unique_sequences = set().union(*buyers)
        return max(
            sum(buyer.get(sequence, 0) for buyer in buyers)
            for sequence in unique_sequences
        )


if __name__ == "__main__":
    Today().solve()
