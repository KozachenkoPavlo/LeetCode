from typing import List


class Solution:
    # Time: O(2**(2 * N) * N)
    # Space: O(2**(2 * N) * N)
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        item = []

        def callback(open_counter: int, close_counter: int):
            if open_counter == n and close_counter == n:
                result.append("".join(item))
                return

            if open_counter < n:
                item.append("(")
                callback(open_counter + 1, close_counter)
                item.pop()

            if close_counter < open_counter:
                item.append(")")
                callback(open_counter, close_counter + 1)
                item.pop()

        callback(0, 0)

        return result
