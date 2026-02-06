from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full_sum = 0

        for i, n in enumerate(nums, start=1):
            full_sum += (i - n)

        return full_sum
