from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1, p2 = 0, 0

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

            p2 += 1
