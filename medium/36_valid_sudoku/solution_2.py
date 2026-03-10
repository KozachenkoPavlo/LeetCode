from typing import List


class Solution:
    def add_to_checker(self, checker: set, value: int | str):
        if value == ".":
            return True

        if value in checker:
            return False

        checker.add(value)

        return True

    # Time: O(n)
    # Space: O(3n) -> O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        horizontals = [set() for _ in range(size)]
        verticals = [set() for _ in range(size)]
        sections = [set() for _ in range(size)]

        for row in range(size):
            for col in range(size):
                value = board[row][col]
                if not (
                        self.add_to_checker(horizontals[row], value)
                        and self.add_to_checker(verticals[col], value)
                        and self.add_to_checker(sections[col // 3 * 3 + row // 3], value)
                ):
                    return False

        return True