class Solution:
    # Time: O(N)
    # Space: O(N)
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s * 2)[1:-1]
