from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def get_count_of_soldiers(formation: list) -> int:
            left, right = 0, len(formation) - 1

            while left <= right:
                index = (left + right) // 2

                if formation[index] == 1:
                    left = index + 1
                else:
                    right = index - 1

            return left

        result = []

        for i, m in enumerate(mat):
            value = [i, get_count_of_soldiers(m)]
            result.append(value)

        result.sort(key=lambda x: x[1])

        return [i for i, v in result[:k]]
