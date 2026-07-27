from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            r = 0

            while i != 0:
                r += i & 1
                i >>= 1

            result.append(r)

        return result
