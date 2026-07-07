from typing import Optional

import math

from data_structures import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, min_value, max_value = stack.pop()

            if not (min_value < node.val < max_value):
                return False

            if node.left:
                stack.append((node.left, min_value, node.val))

            if node.right:
                stack.append((node.right, node.val, max_value))

        return True
