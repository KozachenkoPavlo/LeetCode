from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 1

        for n in arr:
            if n - s > 0:
                for i in range(n - s, 0, -1):
                    if k == 1:
                        return n - i
                    else:
                        k -= 1
            s = n + 1

        return n + k
