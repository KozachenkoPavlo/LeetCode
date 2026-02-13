from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        arr2.sort()

        for val in arr1:
            closest = bisect_left(arr2, val)

            # Check left neighbour
            if closest > 0 and abs(val - arr2[closest - 1]) <= d:
                continue

            # Check right neighbour
            if closest < len(arr2) and abs(val - arr2[closest]) <= d:
                continue

            result += 1

        return result
