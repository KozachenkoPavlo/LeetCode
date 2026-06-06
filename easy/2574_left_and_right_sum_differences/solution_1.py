from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]
        result = []

        for i in range(len(nums) - 1):
            left_sum.append(left_sum[-1] + nums[i])

        for i in range(len(nums) - 1, 0, -1):
            right_sum.append(right_sum[-1] + nums[i])

        right_sum.reverse()

        for i, j in zip(left_sum, right_sum):
            result.append(abs(i - j))

        return result
