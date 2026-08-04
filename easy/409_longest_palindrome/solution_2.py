from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        result = 0

        for value in counter.values():
            result += value // 2 * 2

        for value in counter.values():
            if value % 2 == 1:
                return result + 1

        return result
