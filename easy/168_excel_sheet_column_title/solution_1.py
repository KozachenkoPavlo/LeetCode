class Solution:
    def num_to_letter(self, num: int) -> str:
        if not (0 <= num < 27):
            raise RuntimeError(f"Number should be in range from 0 to 26. Gotten: {num}")

        return chr(65 + num)

    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber != 0:
            left = (columnNumber - 1) % 26
            result.append(left)

            columnNumber = (columnNumber - 1) // 26

        return "".join([self.num_to_letter(num) for num in result[::-1]])