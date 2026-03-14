from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(height)):
            while len(stack) > 0 and stack[-1][1] < height[i]:
                result += min(stack[0][1], height[i]) - stack[-1][1]

                if len(stack) > 1:
                    result += (stack[-1][0] - stack[-2][0] - 1) * (min(height[i], stack[0][1]) - stack[-1][1])

                stack.pop()

            stack.append((i, height[i]))

        return result
