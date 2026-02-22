from bisect import bisect_left
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c = 0

        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] > target:
                break

            c += bisect_left(nums[i + 1:], target - nums[i])

        return c
