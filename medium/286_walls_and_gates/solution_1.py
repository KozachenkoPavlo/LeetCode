from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height = len(grid)
        width = len(grid[0])
        seen = set()
        queue = deque([])

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

                    while queue:
                        r, c, d = queue.popleft()

                        if grid[r][c] > d:
                            grid[r][c] = d
                        else:
                            if (r, c) in seen:
                                continue

                        seen.add((r, c))

                        if c + 1 < width and grid[r][c + 1] not in {0, -1}:
                            queue.append((r, c + 1, d + 1))
                        if r + 1 < height and grid[r + 1][c] not in {0, -1}:
                            queue.append((r + 1, c, d + 1))
                        if c > 0 and grid[r][c - 1] not in {0, -1}:
                            queue.append((r, c - 1, d + 1))
                        if r > 0 and grid[r - 1][c] not in {0, -1}:
                            queue.append((r - 1, c, d + 1))
