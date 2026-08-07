class MaxList:
    def __init__(self, size: int):
        self.list = list()
        self.size = size

    def _insert(self, num: int) -> None:
        for i in range(len(self.list)):
            if num > self.list[i]:
                self.list.insert(i, num)
                return

        self.list.append(num)

    def append(self, num: int) -> None:
        if num in self.list:
            return

        if len(self.list) < self.size:
            self._insert(num)
            return

        if self.list[-1] < num:
            self.list.pop()
            self._insert(num)
            return

    def get_sized_max(self) -> int:
        if len(self.list) == self.size:
            return self.list[-1]
        else:
            return self.list[0]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = MaxList(3)

        for num in nums:
            result.append(num)

        return result.get_sized_max()
