from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0
        stack = []
        new_stack = [root]

        while new_stack:
            stack = new_stack.copy()
            new_stack.clear()
            result += 1
            while stack:
                node = stack.pop()
                if node is not None:
                    if node.left is not None:
                        new_stack.append(node.left)
                    if node.right is not None:
                        new_stack.append(node.right)

        return result