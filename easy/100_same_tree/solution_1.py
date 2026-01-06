from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.tree_to_list(p) == self.tree_to_list(q)

    def tree_to_list(self, tree: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [tree]

        while stack:
            node = stack.pop(0)
            if node is not None:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                result.append(None)

        return result
