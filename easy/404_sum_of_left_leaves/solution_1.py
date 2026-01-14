from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def helper(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        if node.left is not None:
            if node.left.left is None and node.left.right is None:
                return node.left.val + helper(node.right)

        return helper(node.left) + helper(node.right)

    return helper(root)
