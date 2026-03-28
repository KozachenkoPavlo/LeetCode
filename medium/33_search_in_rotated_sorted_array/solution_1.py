from typing import List


class Solution:
    # Time: O(log N)
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r - 1:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m
            else:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m

        if target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        else:
            return -1