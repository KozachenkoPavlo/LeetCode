from typing import List


class Solution:
    # Time: O(N!)
    # Space: O(N**2), board
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        used_rows = set()
        used_diagonals_main = set()
        used_diagonals_anti = set()
        result = []

        def is_safe(row: int, col: int) -> bool:
            if row in used_rows:
                return False

            if row - col in used_diagonals_main:
                return False

            if row + col in used_diagonals_anti:
                return False

            return True

        def backtrack(col: int):
            if col == n:
                result.append(["".join(row) for row in board])
                return

            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    used_rows.add(row)
                    used_diagonals_main.add(row - col)
                    used_diagonals_anti.add(row + col)

                    backtrack(col + 1)

                    used_diagonals_anti.remove(row + col)
                    used_diagonals_main.remove(row - col)
                    used_rows.remove(row)
                    board[row][col] = "."

        backtrack(0)

        return result
