class Solution:
    # Time: O(N!)
    # Space: O(4 * N) -> O(N)
    def totalNQueens(self, n: int) -> int:
        used_rows = set()
        used_diagonals_main = set()
        used_diagonals_anti = set()
        result = 0

        def backtrack(col: int):
            nonlocal result

            if col == n:
                result += 1
                return

            for row in range(n):
                if (row in used_rows
                        or row - col in used_diagonals_main
                        or row + col in used_diagonals_anti):
                    continue

                used_rows.add(row)
                used_diagonals_main.add(row - col)
                used_diagonals_anti.add(row + col)

                backtrack(col + 1)

                used_diagonals_anti.remove(row + col)
                used_diagonals_main.remove(row - col)
                used_rows.remove(row)

        backtrack(0)

        return result
