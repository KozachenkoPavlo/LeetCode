from typing import List


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        result = [1, 1]

        while rowIndex - 1 > 0:
            row = [1]

            for i in range(len(result) - 1):
                row.append(result[i] + result[i + 1])

            row.append(1)
            result = row.copy()
            rowIndex -= 1

        return result
