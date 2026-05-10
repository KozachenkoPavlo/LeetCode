class Solution:
    # Time: O(N). Hard to say because we delegate work to C
    # Space: O(1)
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
