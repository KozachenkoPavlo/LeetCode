from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def get_negative_count(arr: list) -> int:
            left, right = 0, len(arr) - 1

            while left <= right:
                index = (left + right) // 2

                if arr[index] >= 0:
                    left = index + 1
                else:
                    right = index - 1

            return len(arr) - left

        return sum([get_negative_count(i) for i in grid])
