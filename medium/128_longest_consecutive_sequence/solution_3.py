from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 in unique_nums:
                continue

            result_temp = 1

            while num + 1 in unique_nums:
                result_temp += 1
                num += 1

            result = max(result, result_temp)

        return result