from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1 = []

        for n in nums1:
            if n not in result1:
                result1.append(n)

        result2 = []

        for n in nums2:
            if n in result1 and n not in result2:
                result2.append(n)

        return result2
