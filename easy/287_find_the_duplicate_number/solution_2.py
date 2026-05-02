from typing import List


class Solution:
    # Theoretically this solution is better, but in real life problems it close to always will be an overkill.
    # And for high-level languages it could be even less efficient.
    # Time: O(N)
    # Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
