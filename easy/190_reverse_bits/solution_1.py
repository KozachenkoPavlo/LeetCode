class Solution:
    def reverseBits(self, n: int) -> int:
        bins = bin(n)[2:]
        result = "0" * (32 - len(bins)) + bins

        return int(result[::-1], 2)
