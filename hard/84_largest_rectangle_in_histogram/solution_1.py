from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0

        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                result = max(result, min_height * (j - i + 1))

        return result
