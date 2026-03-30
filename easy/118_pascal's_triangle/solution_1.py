from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for _ in range(numRows - 1):
            new_list = [1]
            for i in range(len(result[-1]) - 1):
                new_list.append(result[-1][i] + result[-1][i + 1])

            new_list.append(1)
            result.append(new_list)

        return result