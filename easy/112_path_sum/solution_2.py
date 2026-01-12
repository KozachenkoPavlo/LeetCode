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

        if root.left is None and root.right is None:
            return target_sum == root.val

        return self.hasPathSum(root.left, target_sum - root.val) or self.hasPathSum(root.right, target_sum - root.val)
