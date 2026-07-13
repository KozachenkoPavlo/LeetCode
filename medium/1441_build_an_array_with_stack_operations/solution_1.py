from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        index = 0

        for num in range(1, n + 1):
            if index >= len(target):
                return result

            result.append("Push")

            if target[index] != num:
                result.append("Pop")
            else:
                index += 1

        return result
