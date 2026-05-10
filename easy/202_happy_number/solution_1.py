from typing import Generator


class Solution:
    # Time: O(N)
    # Space: O(log N)
    def isHappy(self, n: int) -> bool:
        def get_digits(number: int) -> Generator[int]:
            while number > 0:
                number, digit = divmod(number, 10)
                yield digit

        registry = set()

        while n:
            new_n = 0

            for digit in get_digits(n):
                new_n += (digit ** 2)

            if new_n == 1:
                return True

            if new_n in registry:
                return False
            else:
                registry.add(new_n)

            n = new_n

        return False
