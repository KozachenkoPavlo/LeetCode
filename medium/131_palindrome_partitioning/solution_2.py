from typing import List


class Solution:
    # Time: O(N * 2 ** N)
    # Space: O(N ** 2)
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        palindrome_cache = {}

        def is_palindrome(left: int, right: int) -> bool:
            origin_left, origin_right = left, right

            if (left, right) in palindrome_cache:
                return palindrome_cache[(left, right)]

            while left < right:
                if s[left] != s[right]:
                    palindrome_cache[(origin_left, origin_right)] = False
                    return False
                left += 1
                right -= 1

            palindrome_cache[(origin_left, origin_right)] = True
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