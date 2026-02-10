from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int] | None:
        delta = (sum(bobSizes) - sum(aliceSizes)) // 2
        set_a = set(aliceSizes)
        set_b = set(bobSizes)

        for a in set_a:
            b = a + delta
            if b in set_b:
                return [a, b]
