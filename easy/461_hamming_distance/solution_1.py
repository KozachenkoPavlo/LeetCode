import itertools


class Solution:
    # Time: O(log(max(x, y)))
    # Space: O(log(max(x, y)))
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        x = bin(x)[2:]
        y = bin(y)[2:]

        for i, j in itertools.zip_longest(x[::-1], y[::-1], fillvalue="0"):
            if i != j:
                result += 1

        return result
