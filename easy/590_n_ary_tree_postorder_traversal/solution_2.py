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

        # Not necessary for LeetCode, but critical in life
        if root.children is not None:
            for child in root.children:
                result.extend(self.postorder(child))

        result.append(root.val)

        return result
