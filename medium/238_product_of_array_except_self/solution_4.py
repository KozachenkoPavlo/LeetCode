from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = nums[0]

        for i in range(1, len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        suffix = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result