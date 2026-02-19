from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        result = []

        while target in nums:
            t_index = nums.index(target)
            result.append(t_index)
            nums[t_index] -= 1

        return result
