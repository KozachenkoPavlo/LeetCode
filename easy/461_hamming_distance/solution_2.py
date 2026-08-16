class Solution:
    # Time: O(1)
    # Space: O(1)
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
