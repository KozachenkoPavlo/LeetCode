from typing import List


class Solution:
    # Time: O(N)
    # Space: O(1)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0] * 102  # Amount of unique numbers + 1

        for num in nums:
            bucket[num + 1] += 1

        for i in range(1, len(bucket)):
            bucket[i] += bucket[i - 1]

        return [bucket[num] for num in nums]
