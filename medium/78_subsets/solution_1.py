from typing import List


class Solution:
    # Time: O(N * 2 ** N)
    # Space: O(N * 2 ** N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i: int, subset: list) -> None:
            if i == len(nums):
                result.append(subset)
                return

            backtrack(i + 1, subset)
            backtrack(i + 1, subset + [nums[i]])

        backtrack(0, [])

        return result
