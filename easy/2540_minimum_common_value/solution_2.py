from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(arr: list, target: int) -> bool:
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] < target:
                    l = m + 1
                elif arr[m] > target:
                    r = m - 1
                else:
                    return True

            return len(arr) > l and arr[l] == target

        for num in nums1:
            if binary_search(nums2, num):
                return num

        return -1
