class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = mid * (mid + 1) / 2

            if n < result:
                right = mid - 1
            elif n > result:
                left = mid + 1
            else:
                return mid

        return right
