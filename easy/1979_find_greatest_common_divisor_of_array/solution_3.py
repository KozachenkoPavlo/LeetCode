from typing import List


class Solution:
    def get_GCD(self, num1: int, num2: int) -> int:
        while num2 > 0:
            num1, num2 = num2, num1 % num2

        return num1

    def findGCD(self, nums: List[int]) -> int:
        return self.get_GCD(min(nums), max(nums))
