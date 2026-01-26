from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        def get_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return node.val + get_sum(node.left) + get_sum(node.right)

        def dfs(node: TreeNode):
            nonlocal result

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            if node.left or node.right:
                result += abs(get_sum(node.left) - get_sum(node.right))

        dfs(root)

        return result
