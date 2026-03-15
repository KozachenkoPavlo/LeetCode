from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            if height[right] < height[left]:
                result += max_right - height[right]
                right -= 1
            else:
                result += max_left - height[left]
                left += 1

        return result
