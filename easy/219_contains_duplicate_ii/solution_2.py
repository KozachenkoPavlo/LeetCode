from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        registry = {}

        for i, num in enumerate(nums):
            if num in registry and (i - registry[num]) <= k:
                return True
            else:
                registry[num] = i

        return False
