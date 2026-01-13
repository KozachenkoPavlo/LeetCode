from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        def helper(node: Optional[TreeNode]):
            if node is None:
                return

            stack.append(node.val)
            helper(node.right)
            helper(node.left)

        helper(root)

        return stack[::-1]
