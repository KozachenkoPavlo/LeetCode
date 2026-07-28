from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_counter = Counter(magazine)
        r_counter = Counter(ransomNote)

        for key, value in r_counter.items():
            if not (key in m_counter and value <= m_counter[key]):
                return False

        return True
