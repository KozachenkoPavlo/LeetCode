from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums_sum = []
        s = 0

        for n in nums:
            s += n
            self.nums_sum.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            left = self.nums_sum[left - 1]

        return self.nums_sum[right] - left
