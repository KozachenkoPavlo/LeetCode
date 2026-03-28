class TimeMap:
    def _find_floor_index(self, key: str, timestamp: int) -> int:
        left, right = 0, len(self.time_map[key]) - 1

        while left <= right:
            middle = (left + right) // 2

            if self.time_map[key][middle][0] < timestamp:
                left = middle + 1
            elif self.time_map[key][middle][0] > timestamp:
                right = middle - 1
            else:
                return middle

        return right

    def __init__(self):
        self.time_map: dict[str, list[list]] = {}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map.keys():
            self.time_map[key].append([timestamp, value])
        else:
            self.time_map[key] = [[timestamp, value]]

    # Time: O(log N)
    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            index = self._find_floor_index(key, timestamp)

            if index == -1:
                return ""

            return self.time_map[key][index][1]

        return ""

