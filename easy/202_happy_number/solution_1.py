from typing import Generator


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digits(number: int) -> Generator[int]:
            while number:
                yield number % 10
                number = number // 10

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
