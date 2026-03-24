from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            s = 0

            for pile in piles:
                s += (pile + k - 1) // k

            if s > h:
                l = k + 1
            else:
                r = k - 1

        return l
