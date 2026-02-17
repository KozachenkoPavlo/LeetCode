from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums) + 1):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1

            if i == len(nums) - left:
                return i

        return -1
