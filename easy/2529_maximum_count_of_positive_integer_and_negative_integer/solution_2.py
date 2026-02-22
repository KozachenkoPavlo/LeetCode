from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def my_bisect_left(arr: list, target: int):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return l

        def my_bisect_right(arr: list, target: int):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m - 1

            return l

        return max(len(nums) - my_bisect_right(nums, 0), my_bisect_left(nums, 0))
