class HashString:
    def __init__(self, string: str = ""):
        self.hash_map = [0] * 52  # 26 a-z and 26 A-Z

        for letter in string:
            self.add(letter)

    def _map_letter_to_index(self, letter: str) -> int:
        if len(letter) != 1:
            raise ValueError("Value must be a single character a-z or A-Z")

        if 'a' <= letter <= 'z':
            return ord(letter) - ord('a')
        if 'A' <= letter <= 'Z':
            return ord(letter) - ord('A') + 26
        raise ValueError(f"Unsupported value: {letter}")

    def _map_index_to_letter(self, index: int) -> str:
        if len(self.hash_map) <= index < 0:
            raise ValueError(f"Value must be in range(0, {len(self.hash_map) + 1}")

        if index < 26:
            return chr(ord('a') + index)

        return chr(ord('A') + index - 26)

    def add(self, value: str) -> None:
        self.hash_map[self._map_letter_to_index(value)] += 1

    def remove(self, value: str) -> None:
        index = self._map_letter_to_index(value)

        if self.hash_map[index] <= 0:
            raise KeyError(f"The value: {value} couldn't be deleted from the hash\n{self.hash_map}")

        self.hash_map[index] -= 1

    def __contains__(self, other: "HashString") -> bool:
        return all(s >= o for s, o in zip(self.hash_map, other.hash_map))

    def __str__(self):
        result = ""

        for index, value in enumerate(self.hash_map):
            result += self._map_index_to_letter(index) * value

        return result


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = (0, len(s) + 1)

        min_distance = len(t)
        p1, p2 = 0, min_distance

        t_hash = HashString(t)
        s_hash = HashString(s[:p2])

        while True:
            while t_hash in s_hash:
                if result[1] - result[0] > p2 - p1:
                    result = (p1, p2)

                s_hash.remove(s[p1])
                p1 += 1

            if p2 >= len(s):
                break

            s_hash.add(s[p2])
            p2 += 1

        if result[1] - result[0] <= len(s):
            return s[*result]

        return ""


if __name__ == "__main__":
    s = Solution()
    tests = [
        {"args": ("OUZODYXAZV", "XYZ"), "expected": "YXAZ"},
        {"args": ("xyz", "xyz"), "expected": "xyz"},
        {"args": ("ab", "a"), "expected": "a"},
        {"args": ("ab", "b"), "expected": "b"},
        {"args": ("aaa", "aa"), "expected": "aa"},
    ]

    for test in tests:
        args, expected = test["args"], test["expected"]
        result = s.minWindow(*args)

        if expected == result:
            print("PASSED")
        else:
            print(f"Result: {result}, but expected: {expected}")
