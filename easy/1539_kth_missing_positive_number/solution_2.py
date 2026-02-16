from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            missed_nums = arr[mid] - (mid + 1)

            if missed_nums < k:
                left = mid + 1
            else:
                right = mid - 1

        return k + left
