class Solution:
    # Time: O(1), because len(s1) == len(s2) == 4
    # Space: O(1)
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # No swaps
        if s1 == s2:
            return True

        # One swap #1
        if s1[2] + s1[1] + s1[0] + s1[3] == s2:
            return True

        # One swap #2
        if s1[0] + s1[3] + s1[2] + s1[1] == s2:
            return True

        # Two swaps #1
        if s1[2] + s1[3] + s1[0] + s1[1] == s2:
            return True

        return False
