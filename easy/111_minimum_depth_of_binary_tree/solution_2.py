# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        if not root:
            return depth

        stack = [(depth + 1, root)]

        while stack:
            depth, node = stack.pop(0)

            if node.left is None and node.right is None:
                return depth

            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))

        return depth
