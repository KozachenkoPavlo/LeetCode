class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        f1, f2 = 1, 2

        for i in range(n - 2):
            f1, f2 = f2, f1 + f2

        return f2