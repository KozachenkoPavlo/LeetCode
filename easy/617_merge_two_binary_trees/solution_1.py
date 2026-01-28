from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 and node2:
                return TreeNode(
                    node1.val + node2.val,
                    helper(node1.left, node2.left),
                    helper(node1.right, node2.right)
                )
            elif node1:
                return TreeNode(
                    node1.val,
                    helper(node1.left, None),
                    helper(node1.right, None)
                )
            elif node2:
                return TreeNode(
                    node2.val,
                    helper(node2.left, None),
                    helper(node2.right, None)
                )
            else:
                return None

        result = helper(root1, root2)

        return result
