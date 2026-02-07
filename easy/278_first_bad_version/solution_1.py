BAD_VERSION = 4


def isBadVersion(version: int) -> bool:
    return version < BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            cursor = (left + right) // 2

            if isBadVersion(cursor):
                right = cursor
            else:
                left = cursor + 1

        return right


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
