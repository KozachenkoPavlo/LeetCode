from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        registry = {}

        for i in range(len(numbers)):
            num = numbers[i]
            if target - num >= num and num not in registry:
                registry[num] = i
            elif target - num in registry:
                return [registry[target - num] + 1, i + 1]

        return [-1, -1]
