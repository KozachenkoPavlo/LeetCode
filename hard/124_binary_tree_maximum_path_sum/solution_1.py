from collections import deque

import math

from data_structures import TreeNode


class Solution:
    def create_sum_tree(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root

        if not root.right:
            left = self.create_sum_tree(root.left)
            root.val = max(root.val + left.val, root.val)

            return root

        if not root.left:
            right = self.create_sum_tree(root.right)
            root.val = max(root.val + right.val, root.val)

            return root

        left = self.create_sum_tree(root.left)
        right = self.create_sum_tree(root.right)
        root.val = max(
            root.val + right.val,
            root.val + left.val,
            root.val
        )

        return root

    def maxPathSum(self, root: TreeNode) -> int:
        sum_tree = self.create_sum_tree(root)
        result = -math.inf

        queue = deque([sum_tree])

        while queue:
            node = queue.popleft()
            result = max(
                result,
                node.left.val if node.left else -math.inf,
                node.right.val if node.right else -math.inf,
                node.val + min(node.right.val, node.left.val) if node.left and node.right else -math.inf,
                node.val,
            )

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
