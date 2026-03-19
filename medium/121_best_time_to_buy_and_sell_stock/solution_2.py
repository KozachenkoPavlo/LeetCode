from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while len(prices) > r > l:
            if r < len(prices) - 1 and prices[r] < prices[r + 1]:
                r += 1
                continue

            if l < len(prices) - 1 and prices[l] > prices[l + 1] and l < r - 1:
                l += 1
                continue

            result = max(result, prices[r] - prices[l])

            if len(prices) - 1 > r > l:
                r += 1
            else:
                l += 1

        return result
