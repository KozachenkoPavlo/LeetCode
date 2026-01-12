# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False

        stack = [(root.val, root)]
        leaf_sum = []

        while stack:
            s, node = stack.pop(0)

            if node.left is None and node.right is None:
                leaf_sum.append(s)

            if node.left is not None:
                stack.append((s + node.left.val, node.left))
            if node.right is not None:
                stack.append((s + node.right.val, node.right))

        return target_sum in leaf_sum
