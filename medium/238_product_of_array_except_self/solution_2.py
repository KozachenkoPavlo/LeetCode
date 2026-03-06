from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_array[i] = prefix_array[i - 1] * nums[i - 1]
            suffix_array[-i - 1] = suffix_array[-i] * nums[-i]

        return [i * j for i, j in zip(prefix_array, suffix_array)]
