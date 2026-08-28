from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        queue = deque()

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        m = 0

        while queue:
            row, col, m = queue.popleft()

            if row > 0 and grid[row - 1][col] not in {0, 2}:
                grid[row - 1][col] = 2
                queue.append((row - 1, col, m + 1))

            if col > 0 and grid[row][col - 1] not in {0, 2}:
                grid[row][col - 1] = 2
                queue.append((row, col - 1, m + 1))

            if row + 1 < height and grid[row + 1][col] not in {0, 2}:
                grid[row + 1][col] = 2
                queue.append((row + 1, col, m + 1))

            if col + 1 < width and grid[row][col + 1] not in {0, 2}:
                grid[row][col + 1] = 2
                queue.append((row, col + 1, m + 1))

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    return -1

        return m
