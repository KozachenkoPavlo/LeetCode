from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = set()

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            result.add(node.val)
            dfs(node.right)

        dfs(root)

        if len(result) > 1:
            return sorted(list(result))[1]
        else:
            return -1
