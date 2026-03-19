from typing import List

import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = math.inf

        for price in prices:
            if price < min_price:
                min_price = min(min_price, price)

            result = max(result, price - min_price)

        return result
