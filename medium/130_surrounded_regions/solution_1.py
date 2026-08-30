from collections import deque
from typing import List


class Solution:
    # Time: O(N * M)
    # Space: O(N * M)
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])
        queue = deque()
        protected = set()

        for row in range(height):
            for col in range(width):
                if (row == 0 or col == 0 or row == height - 1 or col == width - 1) and board[row][col] == "O":
                    protected.add((row, col))
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for r, c in directions:
                n_row = row + r
                n_col = col + c

                if 0 <= n_row < height and 0 <= n_col < width and (n_row, n_col) not in protected and board[n_row][
                    n_col] == "O":
                    protected.add((n_row, n_col))
                    queue.append((n_row, n_col))

        for row in range(height):
            for col in range(width):
                if (row, col) not in protected and board[row][col] == "O":
                    board[row][col] = "X"
