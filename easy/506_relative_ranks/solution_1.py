from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        length = len(score)
        result = [""] * length
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_score = sorted([(s, i) for i, s in enumerate(score)], reverse=True)

        for i in range(length):
            if i < 3:
                rank = medals[i]
            else:
                rank = str(i + 1)

            result[sorted_score[i][1]] = rank

        return result
