from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r - 1:
            m = (l + r) // 2

            if nums[m] >= nums[r]:
                l = m
            else:
                r = m

        return min(nums[l], nums[r])
