from typing import List


class Solution:
    # Time: O(V + E)
    # Space: O(V + E)
    # V - Vertexes, E - Edges
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        group_counter = 0

        for node in range(n):
            current_len = len(visited)

            dfs(node)

            if current_len != len(visited):
                group_counter += 1

        return group_counter
