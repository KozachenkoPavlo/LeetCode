from typing import List


class Solution:
    # Time: O(3n) -> O(n)
    # Space: O(2*n) -> O(n)
    def trap(self, height: List[int]) -> int:
        result = 0

        max_lefts = [0]
        max_rights = [0]

        max_left = 0
        max_right = 0

        for i in range(len(height)):
            max_left = max(max_left, height[i])
            max_lefts.append(max_left)

        for i in range(len(height) - 1, -1, -1):
            max_right = max(max_right, height[i])
            max_rights.append(max_right)

        max_rights.reverse()

        for i in range(len(height)):
            r = min(max_lefts[i], max_rights[i]) - height[i]

            if r > 0:
                result += r

        return result