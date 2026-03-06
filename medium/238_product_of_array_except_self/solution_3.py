from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    #
    # This solution is not faster than solution_4.py because
    # Deeply it is faster to go from one side to another
    # than try to reach beginning and ending at the same time
    #
    # Why?
    # Because of cache thrashing
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