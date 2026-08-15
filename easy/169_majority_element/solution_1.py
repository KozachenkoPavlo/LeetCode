from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        registry = {}
        half_count_nums = (len(nums) + 1) // 2

        for num in nums:
            if num in registry:
                registry[num] += 1

                if registry[num] >= half_count_nums:
                    return num
            else:
                registry[num] = 1

        return -1
