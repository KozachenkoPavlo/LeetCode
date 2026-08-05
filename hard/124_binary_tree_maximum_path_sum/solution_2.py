import math

from data_structures import TreeNode


class Solution:
    result: int | float

    def maxPathSum(self, root: TreeNode) -> int:
        def get_max_branch(node: TreeNode) -> int:
            if not node:
                return 0

            left_sum = max(0, get_max_branch(node.left))
            right_sum = max(0, get_max_branch(node.right))
            result = node.val + max(left_sum, right_sum)
            self.result = max(self.result, node.val + left_sum + right_sum)

            return result

        self.result = -math.inf
        get_max_branch(root)

        return self.result
