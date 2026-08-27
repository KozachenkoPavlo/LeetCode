class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        result = list(s)

        for i in range(0, len(s), 2 * k):
            if i + k - 1 < len(s):
                j = i + k - 1
            else:
                j = len(s) - 1

            while i < j:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1

        return "".join(result)
