class Solution:
    # Time: O(N), where N is a length of bits
    # Space: O(1)
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n:
            if n & 1:
                result += 1
            n = n >> 1

        return result
