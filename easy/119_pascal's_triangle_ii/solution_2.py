from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(1, rowIndex + 1):
            result.append(int(result[-1] * (rowIndex - i + 1) / i))

        return result
