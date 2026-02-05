from typing import Optional, Generator


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # TODO: Try to solve it calculating numbers using depth, it seems it could work.
        # Starting from leafs ending with the root
        # return 2 ** depth, for leaf it is 1 or 0, for their parents it is 2 or 0, 4 or 0 and so on
        pass