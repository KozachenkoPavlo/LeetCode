from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set2 = set(nums2)

        for i in nums1:
            if i in set2:
                return i

        return -1
