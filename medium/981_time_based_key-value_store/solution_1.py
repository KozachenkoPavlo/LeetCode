class TimeMap:
    def _find_floor_index(self, key: str, timestamp: int) -> int:
        for index, value in enumerate(self.time_map[key]):
            if value[0] > timestamp:
                return index - 1

        return len(self.time_map[key]) - 1

    def __init__(self):
        self.time_map: dict[str, list[tuple[int, str]]] = {}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = [(timestamp, value)]

    # Time: O(N)
    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            index = self._find_floor_index(key, timestamp)

            if index == -1:
                return ""

            return self.time_map[key][index][1]

        return ""
