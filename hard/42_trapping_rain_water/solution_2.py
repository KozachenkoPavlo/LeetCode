from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom_height = height[stack.pop()]

                if not stack:
                    break

                width = i - stack[-1] - 1
                h = min(height[stack[-1]], height[i]) - bottom_height
                result += width * h

            stack.append(i)

        return result
