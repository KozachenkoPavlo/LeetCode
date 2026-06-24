from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1, p2 = 0, k
        result = []

        while p2 <= len(nums):
            result.append(max(nums[p1:p2]))
            p1 += 1
            p2 += 1

        return result
