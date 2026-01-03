class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        fibonacci = [1, 2]

        for i in range(n - 2):
            fibonacci.append(fibonacci[-2] + fibonacci[-1])

        return fibonacci[-1]
