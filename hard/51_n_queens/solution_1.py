from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []

        def is_save(row: int, col: int) -> bool:
            # horizontally
            for c in range(col):
                if board[row][c] == "Q":
                    return False

            # top-left diagonally
            c = col - 1
            r = row - 1
            while c > -1 and r > -1:
                if board[r][c] == "Q":
                    return False
                c -= 1
                r -= 1

            # bottom-left diagonally
            c = col - 1
            r = row + 1
            while c > -1 and r < n:
                if board[r][c] == "Q":
                    return False
                c -= 1
                r += 1

            return True

        def backtrack(col: int):
            for row in range(n):
                if is_save(row, col):
                    board[row][col] = "Q"

                    if col + 1 == n:
                        result.append(["".join(row) for row in board])
                    else:
                        backtrack(col + 1)

                    board[row][col] = "."

        backtrack(0)

        return result
