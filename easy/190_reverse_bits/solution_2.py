class Solution:
    def reverseBits(self, n: int) -> int:
        bits = 32
        result = 0

        for i in range(bits - 1, -1, -1):
            result += (n // 2 ** i) * 2 ** (bits - i - 1)
            n %= 2 ** i

        return result
