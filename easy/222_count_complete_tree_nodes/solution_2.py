from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        node = root

        while True:
            node = node.left
            if node is None:
                break
            depth += 1

        if depth == 0:
            return 1

        left = 2 ** depth
        right = 2 ** (depth + 1)

        def node_exist(n: int) -> bool:
            target = root
            trace = bin(n)[3:]

            while trace:
                step = trace[0]
                trace = trace[1:]

                if step == '0':
                    target = target.left
                else:
                    target = target.right

            return target is not None

        while left < right:
            mid = (left + right) // 2
            if node_exist(mid):
                left = mid + 1
                result = mid
            else:
                right = mid

        return result
