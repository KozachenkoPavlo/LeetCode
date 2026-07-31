from typing import List, Tuple


class Solution:
    def bin_to_time(self, hour_map: List[bool], minute_map: List[bool]) -> str | None:
        start_hour = 8
        start_minute = 32
        hours = 0
        minutes = 0

        for hour in hour_map:
            if hour:
                hours += start_hour
            start_hour >>= 1

        for minute in minute_map:
            if minute:
                minutes += start_minute
            start_minute >>= 1

        if hours > 11 or minutes > 59:
            return None

        return f"{hours}:{minutes:02}"

    def map_num_into_hour_minute(self, number: int) -> Tuple[list[bool], list[bool]]:
        hours_minutes = [False] * 10
        index = 9

        while number:
            if number & 1:
                hours_minutes[index] = True

            number >>= 1
            index -= 1

        return hours_minutes[:4], hours_minutes[4:]

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for i in range(1024):
            if turnedOn == i.bit_count():
                time_str = self.bin_to_time(*self.map_num_into_hour_minute(i))

                if time_str is not None:
                    result.append(time_str)

        return result
