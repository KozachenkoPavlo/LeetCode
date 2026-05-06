class Solution:
    def reverseBits(self, n: int) -> int:
        bits = 32
        result = 0

        for i in range(bits - 1, -1, -1):
            result = result << 1
            if n & 1:
                result += 1
            n = n >> 1

        return result
