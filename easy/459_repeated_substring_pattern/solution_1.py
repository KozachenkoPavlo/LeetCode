class Solution:
    # Time: O(N ** 2), because concatenation is O(N)
    # Space: O(N)
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i:] + s[:i] == s:
                return True

        return False
