from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start_index = 0
        count = 0

        for num in nums:
            if num < target:
                start_index += 1
            elif num == target:
                count += 1

        return list(range(start_index, start_index + count))
