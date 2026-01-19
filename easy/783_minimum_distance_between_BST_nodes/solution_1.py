# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 100_000
        prev_val = None

        def dfs(node: TreeNode):
            nonlocal result, prev_val

            if node.left:
                dfs(node.left)

            if prev_val is not None:
                result = min(result, node.val - prev_val)

            prev_val = node.val

            if node.right:
                dfs(node.right)

        dfs(root)

        return result
