from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root_1: Optional[TreeNode], root_2: Optional[TreeNode]):
            if root_1 is None and root_2 is None:
                return True

            if root_1 is None or root_2 is None:
                return False

            if root_1.val == root_2.val:
                return isSame(root_1.left, root_2.left) and isSame(root_1.right, root_2.right)

            return False

        stack = [root]

        while stack:
            node = stack.pop(0)
            if isSame(node, subRoot):
                return True

            if node:
                stack.append(node.left)
                stack.append(node.right)

        return False
