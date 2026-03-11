from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            result = numbers[l] + numbers[r]

            if target < result:
                r -= 1
            elif target > result:
                l += 1
            else:
                return [l + 1, r + 1]

        return [-1, -1]