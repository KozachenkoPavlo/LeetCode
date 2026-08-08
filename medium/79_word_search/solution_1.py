from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        def dfs(row: int, col: int, index: int) -> bool:
            if len(word) == index:
                return True

            if (row < 0 or row >= height
                    or col < 0 or col >= width
                    or word[index] != board[row][col]):
                return False

            char = board[row][col]
            board[row][col] = "*"

            result = (
                    dfs(row + 1, col, index + 1) or
                    dfs(row - 1, col, index + 1) or
                    dfs(row, col + 1, index + 1) or
                    dfs(row, col - 1, index + 1)
            )

            board[row][col] = char

            return result

        for i in range(height):
            for j in range(width):
                if dfs(i, j, 0):
                    return True

        return False
