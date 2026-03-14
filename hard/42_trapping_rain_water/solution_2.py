from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:
                result += min(height[stack[0]], height[i]) - height[stack[-1]]

                if len(stack) > 1:
                    result += (stack[-1] - stack[-2] - 1) * (min(height[i], height[stack[0]]) - height[stack[-1]])

                stack.pop()

            stack.append(i)

        return result
