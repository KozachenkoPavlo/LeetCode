from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def get_index(self, val: int) -> int:
        left, right = 0, len(self.nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_element = self.nums[mid]
            if mid_element == val:
                return mid
            elif mid_element > val:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def add(self, val: int) -> int:
        index = self.get_index(val)
        self.nums.insert(index, val)

        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
