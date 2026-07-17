from typing import List


class Solution:
    def get_all_divisions(self, num: int) -> List[int]:
        divisions = []

        for n in range(2, num):
            if num % n == 0:
                divisions.append(n)

        return divisions

    def constructRectangle(self, area: int) -> List[int]:
        divisions = self.get_all_divisions(area)
        count = len(divisions)

        if count % 2 == 0:
            if count == 0:
                return [area, 1]

            return [divisions[count // 2], divisions[count // 2 - 1]]
        else:
            same_num = divisions[count // 2]

            return [same_num, same_num]
