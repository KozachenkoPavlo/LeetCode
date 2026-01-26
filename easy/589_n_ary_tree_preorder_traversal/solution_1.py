from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node: 'Node'):
            nonlocal result

            result.append(node.val)

            for child in node.children:
                dfs(child)

        if root:
            dfs(root)

        return result
