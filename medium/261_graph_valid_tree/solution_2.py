from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False

        nodes = {i: set() for i in range(n)}

        for n1, n2 in edges:
            nodes[n1].add(n2)
            nodes[n2].add(n1)

        visited = set()

        def dfs(node: int):
            if node in visited:
                return

            visited.add(node)

            for neighbor in nodes[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n
