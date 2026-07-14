from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices.copy()

        for index, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                r_index, r_price = stack.pop()
                result[r_index] = r_price - price

            stack.append((index, price))

        return result
