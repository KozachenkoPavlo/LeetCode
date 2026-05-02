from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def findDuplicate(self, nums: List[int]) -> int:
        uniques = set()

        for num in nums:
            if num in uniques:
                return num
            else:
                uniques.add(num)

        return -1
