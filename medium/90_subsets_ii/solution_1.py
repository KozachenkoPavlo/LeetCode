from typing import List


class Solution:
    # Time: O(N * 2 ** N)
    # Space: O(N * 2 ** N)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        nums.sort()

        def backtrace(index: int):

            result.append(subset.copy())

            for i in range(index, len(nums)):
                if index != i and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])

                backtrace(i + 1)

                last_num = subset.pop()

        backtrace(0)

        return result
