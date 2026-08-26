from typing import Optional

from data_structures import GraphNode as Node


class Solution:
    # Time: O(V + E), V - vertices, E - edges
    # Space: O(2 * V) -> O(V), recursion and map
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new_map = {}

        def clone(node: Node):
            if node in old_new_map:
                return old_new_map[node]

            new_node = Node(node.val)
            old_new_map[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))

            return new_node

        return clone(node) if node else None
