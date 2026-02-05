from typing import Optional, Generator


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs_gen(node: Optional[TreeNode], head: str = "") -> Generator[int]:
            if not node:
                yield 0

            if node.left:
                yield from dfs_gen(node.left, head + str(node.val))
            if node.right:
                yield from dfs_gen(node.right, head + str(node.val))

            if not node.left and not node.right:
                yield int(head + str(node.val), 2)

        return sum([num for num in dfs_gen(root)])
