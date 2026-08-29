from collections import deque
from typing import List


class Solution:
    # Time: O(N * M)
    # Space: O(N * M)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])
        pacific, atlantic = set(), set()

        p_queue = deque()
        a_queue = deque()

        for row in range(height):
            for col in range(width):
                if row == 0 or col == 0:
                    p_queue.append((row, col))
                    pacific.add((row, col))
                if row == height - 1 or col == width - 1:
                    a_queue.append((row, col))
                    atlantic.add((row, col))

        def bfs(queue: deque[tuple[int, int]], set_cells: set[tuple[int, int]]):
            while queue:
                row, col = queue.popleft()

                current_height = heights[row][col]
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for r, c in directions:
                    new_row = row + r
                    new_col = col + c

                    if (
                            0 <= new_row < height
                            and 0 <= new_col < width
                            and (new_row, new_col) not in set_cells
                            and current_height <= heights[new_row][new_col]
                    ):
                        set_cells.add((new_row, new_col))
                        queue.append((new_row, new_col))

        bfs(p_queue, pacific)
        bfs(a_queue, atlantic)

        return [[row, col] for row, col in pacific & atlantic]
