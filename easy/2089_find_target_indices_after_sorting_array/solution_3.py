from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        def my_bisect_left(arr: list, t: int) -> int:
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] < t:
                    l = m + 1
                else:
                    r = m - 1

            return l

        def my_bisect_right(arr: list, t: int) -> int:
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2

                if arr[m] <= t:
                    l = m + 1
                else:
                    r = m - 1

            return l

        return list(range(my_bisect_left(nums, target), my_bisect_right(nums, target)))
