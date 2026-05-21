from typing import List


class Solution:
    # Time: O(N * K)
    # Space: O(1)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        for i in range(1, len(nums)):
            j = max(0, i - k)

            for j in range(max(0, i - k), i):
                if nums[i] == nums[j]:
                    return True

        return False
