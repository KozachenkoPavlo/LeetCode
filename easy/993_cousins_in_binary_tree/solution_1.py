from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        stack = [(root, None)]
        floor = []

        while stack:
            matching = {x, y}
            parents = set()
            floor.extend(stack)
            stack.clear()

            while floor:
                node, parent = floor.pop(0)
                if node.val in matching:
                    parents.add(parent)
                    matching.remove(node.val)

                if node.left:
                    stack.append((node.left, node.val))
                if node.right:
                    stack.append((node.right, node.val))

            if not matching:
                if len(parents) == 2:
                    return True
                else:
                    return False

        return False
