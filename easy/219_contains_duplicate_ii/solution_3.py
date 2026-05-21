from typing import List


class Solution:
    # Time: O(N)
    # Space: O(K)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        registry = set()

        for i, num in enumerate(nums):
            if num in registry:
                return True

            registry.add(num)

            if len(registry) > k:
                registry.remove(nums[i - k])

        return False
