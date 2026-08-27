class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        result = list(s)

        for i in range(0, len(s), 2 * k):
            result[i:i + k] = reversed(result[i:i + k])

        return "".join(result)
