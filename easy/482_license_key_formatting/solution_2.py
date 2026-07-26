class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = s.replace("-", "").upper()[::-1]
        groups = []

        for i in range(0, len(result), k):
            groups.append(result[i:i + k])

        return "-".join(groups)[::-1]