from typing import List


class Solution:
    # Time: O(N * 2 ** N)
    # Space: O(N)
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        def backtrace(index: int):
            if index >= len(s):
                result.append(current.copy())
                return

            for i in range(index, len(s)):
                if not is_palindrome(index, i):
                    continue

                current.append(s[index:i + 1])

                backtrace(i + 1)

                current.pop()

        backtrace(0)

        return result
