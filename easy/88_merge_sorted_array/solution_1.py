from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0

        while nums2 and len(nums1) > i:
            if nums1[i] >= nums2[0]:
                nums1.insert(i, nums2.pop(0))
                nums1.pop()
            else:
                i += 1

        for _ in range(len(nums2)):
            nums1.pop()

        for i in nums2:
            nums1.append(i)
