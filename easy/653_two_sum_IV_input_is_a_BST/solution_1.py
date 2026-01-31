from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root or not (root.left or root.right):
            return False

        def dfs(node: TreeNode) -> TreeNode:
            if node.left:
                yield from dfs(node.left)

            yield node

            if node.right:
                yield from dfs(node.right)

        def dls(node: TreeNode) -> TreeNode:
            if node.right:
                yield from dls(node.right)

            yield node

            if node.left:
                yield from dls(node.left)

        left_pointer_gen = dfs(root)
        right_pointer_gen = dls(root)

        left_pointer = next(left_pointer_gen)
        right_pointer = next(right_pointer_gen)

        while left_pointer.val < right_pointer.val:
            result = left_pointer.val + right_pointer.val

            if result < k:
                left_pointer = next(left_pointer_gen)
            elif result > k:
                right_pointer = next(right_pointer_gen)
            else:
                return True

        return False
