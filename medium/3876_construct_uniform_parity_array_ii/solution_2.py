from math import inf
from typing import List


class Solution:
    # Time: O(N)
    # Space: O(1)
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = inf
        min_even = inf

        for num in nums1:
            if num % 2 == 1:
                min_odd = min(min_odd, num)
            else:
                min_even = min(min_even, num)

        if min_odd == inf or min_even == inf:
            return True

        return min_odd <= min_even
