from typing import List


class Solution:
    # Time: O(N * N!)
    # Space: O(N * N!), with a result
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        excluded_index = set()

        def dfs() -> None:
            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):
                if i in excluded_index:
                    continue

                subset.append(nums[i])
                excluded_index.add(i)

                dfs()

                excluded_index.remove(i)
                subset.pop()

        dfs()

        return result
