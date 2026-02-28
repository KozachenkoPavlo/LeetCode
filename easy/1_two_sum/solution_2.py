from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        registry = {}

        for i in range(len(nums)):
            registry[nums[i]] = i

        for i in range(len(nums)):
            t = target - nums[i]
            if t in registry and registry[t] != i:
                return [i, registry[t]]
