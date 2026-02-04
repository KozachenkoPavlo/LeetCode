from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        broken_tree = TreeNode(0)
        pointer = broken_tree

        def dfs(node: Optional[TreeNode]):
            if not node:
                return None

            if node.left:
                yield from dfs(node.left)

            yield node.val

            if node.right:
                yield from dfs(node.right)

        for value in dfs(root):
            pointer.right = TreeNode(value)
            pointer = pointer.right

        return broken_tree.right
