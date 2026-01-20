from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []

        def helper(node: 'Node') -> None:
            if node.children:
                for child in node.children:
                    helper(child)

            result.append(node.val)

        helper(root)

        return result
