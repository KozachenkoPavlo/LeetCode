from typing import List


class Solution:
    def rotate_in_range(self, left: int, right: int, array: list):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # Time: O(N)
    # Space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums.reverse()

        self.rotate_in_range(0, k - 1, nums)
        self.rotate_in_range(k, len(nums) - 1, nums)