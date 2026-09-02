from typing import List


class Solution:
    # Time: O(N)
    # Space: O(N)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False

        if len(edges) == 0:
            return True

        nodes = {i: set() for i in range(n)}

        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])

        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in nodes[node]:
                nodes[neighbor].remove(node)
                if not dfs(neighbor):
                    return False

            return True

        if not dfs(edges[0][0]):
            return False

        return len(visited) == n
