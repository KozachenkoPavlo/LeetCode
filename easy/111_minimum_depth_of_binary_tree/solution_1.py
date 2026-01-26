from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        depth = 0

        while stack:
            working_stack = stack.copy()
            stack.clear()

            while working_stack:
                node = working_stack.pop(0)

                if not node:
                    continue

                if node.left is None and node.right is None:
                    return depth + 1
                else:
                    stack.append(node.left)
                    stack.append(node.right)

            depth += 1

        return depth
