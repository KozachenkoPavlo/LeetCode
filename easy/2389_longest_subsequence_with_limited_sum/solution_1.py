from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        result = []

        for q in queries:
            c = 0
            while q > 0 and c < len(nums):
                q -= nums[c]
                c += 1

            if q < 0:
                c -= 1

            result.append(c)

        return result
