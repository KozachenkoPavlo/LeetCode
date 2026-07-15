from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        length = len(score)
        result = [""] * length
        sorted_score = sorted([(s, i) for i, s in enumerate(score)], reverse=True)

        for i in range(length):
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i + 1)

            result[sorted_score[i][1]] = rank

        return result
