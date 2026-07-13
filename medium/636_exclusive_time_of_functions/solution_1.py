from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev_time = 0
        stack = []
        result = [0] * n

        for log in logs:
            parsed_log = log.split(":")
            fun_id, action, time = int(parsed_log[0]), parsed_log[1], int(parsed_log[2])

            if action == "start":
                if stack:
                    result[stack[-1]] += time - prev_time - 1

                stack.append(fun_id)
            else:
                result[fun_id] += time - prev_time + 1
                stack.pop()

            prev_time = time

        return result
