from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            index = (left + right) // 2

            if letters[index] <= target:
                left = index + 1
            else:
                right = index - 1

        if letters[-1] <= target:
            return letters[0]

        return letters[left]
