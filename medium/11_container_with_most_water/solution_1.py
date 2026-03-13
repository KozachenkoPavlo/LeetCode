from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                volume = (right - left) * heights[left]
                left += 1
            else:
                volume = (right - left) * heights[right]
                right -= 1

            result = max(result, volume)

        return result