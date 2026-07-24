from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0

        for i in range(len(nums)):
            if nums[i - count] == 0:
                del nums[i - count]
                count += 1

        for _ in range(count):
            nums.append(0)
