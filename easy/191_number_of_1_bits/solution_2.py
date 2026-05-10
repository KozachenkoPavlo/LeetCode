class Solution:
    # Time: O(N), where N is a count of ones
    # Space: O(1)
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n:
            n = n & (n - 1)
            result += 1

        return result