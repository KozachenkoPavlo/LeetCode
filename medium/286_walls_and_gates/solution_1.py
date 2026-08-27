from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height = len(grid)
        width = len(grid[0])
        queue = deque([])

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            r, c, d = queue.popleft()

            if c + 1 < width and grid[r][c + 1] == 2147483647:
                grid[r][c + 1] = min(d + 1, grid[r][c + 1])
                queue.append((r, c + 1, d + 1))

            if r + 1 < height and grid[r + 1][c] == 2147483647:
                grid[r + 1][c] = min(d + 1, grid[r + 1][c])
                queue.append((r + 1, c, d + 1))

            if c > 0 and grid[r][c - 1] == 2147483647:
                grid[r][c - 1] = min(d + 1, grid[r][c - 1])
                queue.append((r, c - 1, d + 1))

            if r > 0 and grid[r - 1][c] == 2147483647:
                grid[r - 1][c] = min(d + 1, grid[r - 1][c])
                queue.append((r - 1, c, d + 1))
