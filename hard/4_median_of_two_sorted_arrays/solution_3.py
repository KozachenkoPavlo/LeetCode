from typing import List


class Solution:
    # Time: O(log(min(N, M)) where N = len(nums1) and M = len(nums2)
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s_nums, l_nums = nums1, nums2
        if len(s_nums) > len(l_nums):
            s_nums, l_nums = l_nums, s_nums

        total = len(s_nums) + len(l_nums)
        half = total // 2

        left, right = 0, len(s_nums)

        while left <= right:
            i = (left + right) // 2
            j = half - i

            s_left = s_nums[i - 1] if i > 0 else float("-inf")
            s_right = s_nums[i] if i < len(s_nums) else float("inf")

            l_left = l_nums[j - 1] if j > 0 else float("-inf")
            l_right = l_nums[j] if j < len(l_nums) else float("inf")

            if s_left <= l_right and l_left <= s_right:
                if total % 2 == 1:
                    return float(min(s_right, l_right))
                else:
                    return (max(s_left, l_left) + min(s_right, l_right)) / 2

            elif s_left > l_right:
                right = i - 1
            else:
                left = i + 1

        return 0.0
