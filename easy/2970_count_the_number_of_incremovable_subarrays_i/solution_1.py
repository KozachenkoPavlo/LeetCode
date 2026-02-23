from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_incremovable(arr: list) -> bool:
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False

            return True

        result = 0

        for size in range(1, len(nums)):
            index = 0

            while index <= len(nums) - size:
                a = nums[0:index] + nums[size + index:len(nums)]
                p = is_incremovable(a)
                if p:
                    result += 1

                index += 1

        return result + 1
