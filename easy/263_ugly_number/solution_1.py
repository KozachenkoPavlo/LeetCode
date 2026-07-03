class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        nums = [2, 3, 5]

        while n != 1:
            for num in nums:
                if n % num == 0:
                    n = n // num
                    break
            else:
                return False

        return True
