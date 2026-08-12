from typing import List


class Solution:
    # Time: O(N * (2 ** N))
    # 2, because we take or skip a candidate. N for .copy()
    # Space: O(N)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        target_sum = 0

        candidates.sort()

        def dfs(index: int):
            nonlocal target_sum

            if target_sum == target:
                result.append(subset.copy())
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]

                if target_sum + candidate > target:
                    break

                # Another approach
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                target_sum += candidate
                subset.append(candidate)

                dfs(i + 1)

                target_sum -= candidate
                subset.pop()

        dfs(0)
        return result
