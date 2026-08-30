class Solution:
    # Time: O(1)
    # Space: O(1)
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if sum(source) % 2 != sum(target) % 2:
            return -1

        if sum(source) == sum(target) or source[0] - source[1] == target[0] - target[1]:
            return 1

        return 2
