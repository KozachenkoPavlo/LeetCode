from typing import List


class Solution:
    code: str = "#"

    # Time: O(n)
    # Space: O(n * m), n - len(List), m - len(List[])
    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)) + self.code + s)

        return "".join(result)

    # Time: O(n)
    # Space: O(n), n - len(s)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)

        while i < n:
            force = ""

            while s[i] != self.code:
                force += s[i]
                i += 1

            force = int(force)
            i += 1

            result.append(s[i:i + force])

            i += force

        return result
