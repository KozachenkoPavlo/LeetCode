from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        registry = set()

        for num in nums:
            if num in registry:
                return True
            else:
                registry.add(num)

        return False
