class Solution:
    def letter_to_num(self, letter: str) -> int:
        return ord(letter) - 64

    # Time: O(N)
    # Space: O(1)
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for letter in columnTitle:
            result *= 26
            result += self.letter_to_num(letter)

        return result
