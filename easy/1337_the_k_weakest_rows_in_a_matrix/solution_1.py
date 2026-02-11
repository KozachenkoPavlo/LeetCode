from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [(i, m) for i, m in enumerate(mat)]

        def get_count_of_soldiers(formation: list) -> int:
            left, right = 0, len(formation) - 1

            while left <= right:
                index = (left + right) // 2

                if formation[index] == 1:
                    left = index + 1
                else:
                    right = index - 1

            return left

        for i in range(len(mat) + 1):
            for j in range(1, len(mat) - i):

                if get_count_of_soldiers(mat[j][1]) < get_count_of_soldiers(mat[j - 1][1]):
                    mat[j], mat[j - 1] = mat[j - 1], mat[j]

        return [i for i, m in mat[:k]]
