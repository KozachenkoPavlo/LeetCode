from typing import List


class Solution:
    # Time: O(n)
    # Space: O(2*n)
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        unique_nums = set(nums)
        seen = set()

        for num in unique_nums:
            if num in seen:
                continue

            start = num

            while start - 1 in unique_nums:
                start -= 1

            while num + 1 in unique_nums:
                num += 1

            result = max(result, num - start + 1)
            seen.update(list(range(start, num + 1)))

        return result
