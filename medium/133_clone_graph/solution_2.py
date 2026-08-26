from collections import deque
from typing import Optional

from data_structures.graph_node import GraphNode as Node


class Solution:
    # Time: O(V + E), V - vertices, E - edges
    # Space: O(2 * V) -> O, queue and map
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_new_map = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in old_new_map:
                    old_new_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                old_new_map[current_node].neighbors.append(old_new_map[neighbor])

        return old_new_map[node]
