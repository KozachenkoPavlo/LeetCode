from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        stack = [root]
        counter = {}

        while stack:
            node = stack.pop(0)

            if node.val not in counter.keys():
                counter[node.val] = 1
            else:
                counter[node.val] += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        max_value = max(counter.values())

        return [key for key, value in counter.items() if value == max_value]
