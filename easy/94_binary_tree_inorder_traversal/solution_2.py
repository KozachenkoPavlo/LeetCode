from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        head = root

        while head or stack:
            while head:
                stack.append(head)
                head = head.left
            head = stack.pop()
            result.append(head.val)
            head = head.right

        return result
