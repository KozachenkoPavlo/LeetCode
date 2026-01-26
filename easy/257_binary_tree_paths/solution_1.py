from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def helper(node: Optional[TreeNode], path=""):
            if not node:
                return None

            path += str(node.val)

            if node.left:
                helper(node.left, path + "->")
            if node.right:
                helper(node.right, path + "->")

            if not node.left and not node.right:
                result.append(path)

        helper(root)

        return result
