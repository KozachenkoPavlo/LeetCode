from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        queue = []
        result = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1":
                    result += 1
                    queue.append((row, col))

                    while queue:
                        r, c = queue.pop()

                        if grid[r][c] == "0":
                            continue

                        grid[r][c] = "0"

                        if r > 0:
                            queue.append((r - 1, c))
                        if c > 0:
                            queue.append((r, c - 1))
                        if r + 1 < height:
                            queue.append((r + 1, c))
                        if c + 1 < width:
                            queue.append((r, c + 1))

        return result
