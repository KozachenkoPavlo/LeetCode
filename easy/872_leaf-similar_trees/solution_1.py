import itertools
from typing import Generator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs_leaf_gen(node: Optional[TreeNode]) -> Generator[int | None]:
            if not node:
                return None

            if node.left:
                yield from dfs_leaf_gen(node.left)

            if node.right:
                yield from dfs_leaf_gen(node.right)

            if not node.left and not node.right:
                yield node.val

        for node1, node2 in itertools.zip_longest(dfs_leaf_gen(root1), dfs_leaf_gen(root2)):
            if node1 != node2:
                return False

        return True
