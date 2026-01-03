class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        if x < 9:
            return 2

        for i in range(x//2 + 1):
            if i*i == x:
                return i
            elif i*i > x:
                return i - 1