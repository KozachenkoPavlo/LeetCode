class Solution:
    def longestPalindrome(self, s: str) -> int:
        without_pairs = set()

        for i in s:
            if i in without_pairs:
                without_pairs.remove(i)
            else:
                without_pairs.add(i)

        return len(s) - len(without_pairs) + bool(without_pairs)
