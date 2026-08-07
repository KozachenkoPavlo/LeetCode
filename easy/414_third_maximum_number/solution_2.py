from typing import List

import math


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -math.inf
        second = -math.inf
        third = -math.inf

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first < num:
                first, second, third = num, first, second
            elif second < num:
                second, third = num, second
            elif third < num:
                third = num

        if third != -math.inf:
            return third
        else:
            return first
