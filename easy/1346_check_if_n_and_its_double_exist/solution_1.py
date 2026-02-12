from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            target = arr[i] * 2

            for j in range(len(arr)):
                if target == arr[j] and j != i:
                    return True

        return False
