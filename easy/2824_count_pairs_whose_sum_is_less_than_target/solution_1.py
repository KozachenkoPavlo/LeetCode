from bisect import bisect_left
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c = 0

        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] > target:
                break

            index = bisect_left(nums, target - nums[i], i + 1)
            c += index - (i + 1)

        return c
