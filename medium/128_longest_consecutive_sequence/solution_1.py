from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        temp_result = 1 if len(nums) != 0 else 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                temp_result += 1
            else:
                if nums[i - 1] == nums[i]:
                    continue
                result = max(result, temp_result)
                temp_result = 1

        return max(result, temp_result)