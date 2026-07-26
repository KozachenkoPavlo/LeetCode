class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = s.replace("-", "").upper()
        groups = []

        for i in range(len(result), 0, -k):
            group = result[max(0, i - k):i]
            groups.append(group)

        return "-".join(reversed(groups))
