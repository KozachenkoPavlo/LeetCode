from typing import List


class Solution:
    # Time: O(N + M), M <= N by constraints, so we can simplify: O(N)
    # Space: O(N)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        registry = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                registry[stack.pop()] = num
            stack.append(num)

        return [registry.get(num, -1) for num in nums1]
