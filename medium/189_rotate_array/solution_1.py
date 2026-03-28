from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        counter = 0

        while counter < k:
            num = nums.pop()
            nums.insert(0, num)
            counter += 1
