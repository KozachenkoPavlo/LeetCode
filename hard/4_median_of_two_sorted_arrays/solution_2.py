from collections import deque
from typing import List


class Solution:
    # Time: O((N + M) / 2)
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = (len(nums1) + len(nums2))

        if length % 2 == 1:
            q = deque(maxlen=1)
        else:
            q = deque(maxlen=2)

        target = length // 2 + 1
        i, j = 0, 0

        while i + j < target and (i < len(nums1) or j < len(nums2)):
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                q.append(nums1[i])
                i += 1
            else:
                q.append(nums2[j])
                j += 1

        return sum(q) / len(q)