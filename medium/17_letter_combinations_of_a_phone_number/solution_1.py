from typing import List


class Solution:
    # Time: O(N * 4 ** N)
    # Space: O(N)
    # O(2 * N), stack and current
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        registry = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        current = []

        def backtrace(index: int):
            if index == len(digits):
                result.append("".join(current))
                return

            for letter in registry[digits[index]]:
                current.append(letter)

                backtrace(index + 1)

                current.pop()

        backtrace(0)

        return result
