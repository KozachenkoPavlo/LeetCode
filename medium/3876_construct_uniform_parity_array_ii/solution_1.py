from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        odd = [num for num in nums1 if num % 2 == 1]
        even = [num for num in nums1 if num % 2 == 0]

        if not odd or not even:
            return True

        return min(odd) <= min(even)
