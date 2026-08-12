from typing import List


class Solution:
    # Time: O(N * (2 ** N))
    # 2, because we take or skip a candidate. N for .copy()
    # Space: O(N)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        target_sum = 0
        subset = []
        last_pop = None

        candidates.sort()

        def dfs(index: int):
            nonlocal target_sum, last_pop

            if target_sum == target:
                result.append(subset.copy())
                return

            for candidate_index in range(index, len(candidates)):
                candidate = candidates[candidate_index]

                if target_sum + candidate > target:
                    break

                if last_pop == candidate:
                    continue

                target_sum += candidate
                subset.append(candidate)

                dfs(candidate_index + 1)

                target_sum -= candidate
                last_pop = subset.pop()

        dfs(0)

        return result
