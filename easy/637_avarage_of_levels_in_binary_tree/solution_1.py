from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []

        if not root:
            return result

        stack = [root]
        floor = []

        while stack:
            floor = stack.copy()
            stack.clear()
            floor_nodes = len(floor)
            floor_sum = 0

            while floor:
                node = floor.pop(0)
                floor_sum += node.val

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            result.append(floor_sum / floor_nodes)

        return result
