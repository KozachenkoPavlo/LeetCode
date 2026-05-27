from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        sum_nums = sum(nums)
        sum_unique = sum(set(nums))
        sum_ideal = int(((1 + n) / 2) * n)

        duplicate = abs(sum_unique - sum_nums)
        missed = sum_ideal - sum_unique

        return [duplicate, missed]
