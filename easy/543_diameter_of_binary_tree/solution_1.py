# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        def bfs(node: TreeNode):
            nonlocal result

            if node.left:
                bfs(node.left)

            if node.right:
                bfs(node.right)

            if not node.left and not node.right:
                node.depth = 0
            elif not node.left:
                node.depth = node.right.depth + 1
                result = max(result, node.right.depth + 1)
            elif not node.right:
                node.depth = node.left.depth + 1
                result = max(result, node.left.depth + 1)
            else:
                node.depth = max(node.left.depth, node.right.depth) + 1
                result = max(result, node.left.depth + node.right.depth + 2)

        bfs(root)

        return result
