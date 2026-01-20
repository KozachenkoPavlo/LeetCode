from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node: Optional['Node']):
            if not node:
                return

            # Not necessary for LeetCode, but critical in life
            if node.children:
                for child in node.children:
                    dfs(child)

            result.append(node.val)

        result = []

        dfs(root)

        return result
