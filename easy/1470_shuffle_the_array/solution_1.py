from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    # List has length (2 * x)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])

        return result
