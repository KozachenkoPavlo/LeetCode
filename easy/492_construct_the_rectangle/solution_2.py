from typing import List

import math


class Solution:
    # Time: O(sqrt(N))
    # Space: O(1)
    def constructRectangle(self, area: int) -> List[int]:
        square = math.isqrt(area)

        for i in range(square, 0, -1):
            if area % i == 0:
                return [area // i, i]

        raise RuntimeError(f"Unexpected behaviour, for number: {area}")
