from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        suffix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            suffix *= nums[-i]
            result[i] = result[i] * prefix
            result[-i - 1] = result[-i - 1] * suffix

        return result