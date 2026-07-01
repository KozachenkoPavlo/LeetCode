from typing import Optional, List

from data_structures import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stack = [root]
        temp_stack = []
        result = []

        while stack:
            temp_result = []

            while stack:
                temp_stack.append(stack.pop())

            while temp_stack:
                node = temp_stack.pop()
                temp_result.append(node.val)

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

            result.append(temp_result)

        return result
