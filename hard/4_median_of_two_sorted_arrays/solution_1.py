from typing import List


class Solution:
    # Time: O(N + M)
    # Space: O(N + M)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0

        while i < len(nums1) or j < len(nums2):
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        else:
            return nums[len(nums) // 2]
