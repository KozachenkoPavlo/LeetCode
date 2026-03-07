from typing import List


class Solution:
    empty: str = "_empty_"
    separator: str = "_::_"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty

        if len(strs) == 1:
            return strs[0]

        return self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if self.empty == s:
            return []

        if self.separator not in s:
            return [s]

        return s.split(self.separator)