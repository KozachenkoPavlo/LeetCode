from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        for i in range(len(self.nums)):
            if self.nums[i] < val:
                self.nums.insert(i, val)
                break
        else:
            self.nums.append(val)

        return self.nums[self.k - 1]
