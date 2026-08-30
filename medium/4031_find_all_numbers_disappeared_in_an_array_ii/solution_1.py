import heapq


class Solution:
    # Time: O(N * log N)
    # Space: O(N), because we are creating heap
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        result = []

        heapq.heapify(nums)
        while nums and nums[0] < lower:
            heapq.heappop(nums)

        start = lower

        while start <= upper and nums:
            current_lowest = heapq.heappop(nums)

            if start < current_lowest:
                result.append([start, min(current_lowest - 1, upper)])

            start = current_lowest + 1

        if not nums and start <= upper:
            result.append([start, upper])

        return result
