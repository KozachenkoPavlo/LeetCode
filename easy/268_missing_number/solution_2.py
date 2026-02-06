from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for i, n in enumerate(nums, start=1):
            result ^= i ^ n  # Should be a bit faster than + and -

        return result
