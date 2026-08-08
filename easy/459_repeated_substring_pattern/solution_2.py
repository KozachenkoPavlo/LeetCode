class Solution:
    # Time: O(N * log(N))
    # O(N / 2 * N) -> O(N * log(N)), because operation with O(N) executes only when length % i == 0, this gives us O(log N)
    # Space: O(N)
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        for i in range(1, int(length // 2) + 1):
            if length % i == 0 and s[:i] * (length // i) == s:
                return True

        return False
