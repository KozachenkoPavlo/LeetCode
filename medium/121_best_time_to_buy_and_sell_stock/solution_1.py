from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_max = [0] * len(prices)

        current_max = 0

        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            right_max[i] = current_max

        result = 0

        for i in range(len(prices)):
            result = max(result, right_max[i] - prices[i])

        return result
