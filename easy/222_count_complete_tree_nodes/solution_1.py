from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        result = 0

        while stack:
            node = stack.pop(0)

            if node is not None:
                result += 1
                stack.append(node.left)
                stack.append(node.right)

        return result
