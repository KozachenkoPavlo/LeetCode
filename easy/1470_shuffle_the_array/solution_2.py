from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (n * 2)

        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[n + i]

        return result
