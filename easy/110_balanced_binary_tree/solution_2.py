from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def get_level(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1

            node.level = max(get_level(node.left), get_level(node.right)) + 1
            return node.level

        get_level(root)
        stack = [root]

        while stack:
            node = stack.pop(0)

            left_level = node.left.level if node.left else -1
            right_level = node.right.level if node.right else -1

            if abs(left_level - right_level) > 1:
                return False

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return True
