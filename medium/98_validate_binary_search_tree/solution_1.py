from typing import Optional

import math

from data_structures import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [{"node": root, "min": -math.inf, "max": math.inf}]

        while stack:
            obj = stack.pop()
            node = obj["node"]
            min_value = obj["min"]
            max_value = obj["max"]

            if not (min_value < node.val < max_value):
                return False

            if node.left:
                stack.append({
                    "node": node.left,
                    "min": min_value,
                    "max": min(max_value, node.val)
                })

            if node.right:
                stack.append({
                    "node": node.right,
                    "min": max(min_value, node.val),
                    "max": max_value
                })

        return True
