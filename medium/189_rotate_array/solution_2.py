from typing import List


class Solution:
    # Time: O(k * N)
    # Space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums.reverse()

        for _ in range(k):
            num = nums.pop(0)
            nums.append(num)

        nums.reverse()