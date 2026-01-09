from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left >= right:
                return None

            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = helper(left, middle)
            node.right = helper(middle + 1, right)

            return node

        return helper(0, len(nums))
