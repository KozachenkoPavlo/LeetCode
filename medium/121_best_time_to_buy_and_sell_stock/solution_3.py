from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        if not prices: return 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)

            result = max(result, price - min_price)

        return result
