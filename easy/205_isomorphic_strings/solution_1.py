class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        registry_s = {}
        registry_t = {}

        for i in range(len(s)):
            if s[i] not in registry_s:
                registry_s[s[i]] = t[i]
            else:
                if registry_s[s[i]] != t[i]:
                    return False

            if t[i] not in registry_t:
                registry_t[t[i]] = s[i]
            else:
                if registry_t[t[i]] != s[i]:
                    return False

        return True
