from typing import List


class Solution:
    def get_GCD(self, num1: int, num2: int) -> int:
        _min, _max = (num1, num2) if num1 <= num2 else (num2, num1)

        if _max % _min == 0:
            return _min

        result = _min // 2

        while _max % result != 0 or _min % result != 0:
            result -= 1

        return result

    def findGCD(self, nums: List[int]) -> int:
        return self.get_GCD(min(nums), max(nums))
