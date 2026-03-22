from typing import List


class Solution:
    # Time: O(2*n) -> O(n)
    # Space: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        heights.append(0)  # To clear stack in the end

        for i in range(len(heights)):
            h = heights[i]

            while stack and heights[stack[-1]] > h:
                h_pop = stack.pop()
                height = heights[h_pop]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                result = max(result, height * width)

            stack.append(i)

        return result
