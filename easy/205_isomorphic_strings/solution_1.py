class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        registry_s = {}
        registry_t = {}

        for i, j in zip(s, t):
            if i not in registry_s:
                registry_s[i] = j
            else:
                if registry_s[i] != j:
                    return False

            if j not in registry_t:
                registry_t[j] = i
            else:
                if registry_t[j] != i:
                    return False

        return True
