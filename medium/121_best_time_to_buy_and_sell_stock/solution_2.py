from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        result = 0

        while r < len(prices) - 1:
            r += 1

            if prices[l] < prices[r]:
                result = max(result, prices[r] - prices[l])
            else:
                l = r

        return result
