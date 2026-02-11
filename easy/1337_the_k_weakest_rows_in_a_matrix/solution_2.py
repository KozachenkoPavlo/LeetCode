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

        def get_index_to_insert(array: list, target: int) -> int:
            if not array:
                return 0

            left, right = 0, len(array) - 1

            while left <= right:
                index = (left + right) // 2
                print(array, index, target)

                if array[index][1] <= target:
                    left = index + 1
                else:
                    right = index - 1

            return left

        result = []

        for i, m in enumerate(mat):
            value = [i, get_count_of_soldiers(m)]
            index_to_insert = get_index_to_insert(result, value[1])

            result.insert(index_to_insert, value)

        return [i for i, v in result[:k]]
