from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = 0

        if not root:
            return result

        def dfs(node: 'Node'):
            nonlocal result

            if node.children:
                for child in node.children:
                    dfs(child)

            if not node.children:
                node.depth = 0
            else:
                node.depth = max([n.depth for n in node.children]) + 1

            result = max(result, node.depth)

        dfs(root)

        return result + 1
