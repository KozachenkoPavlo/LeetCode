class Solution:
    def arrangeCoins(self, n: int) -> int:
        row_count = 0
        counter = 1

        while n > 0:
            row_count += 1
            n -= counter
            counter += 1

        if n != 0:
            row_count -= 1

        return row_count
