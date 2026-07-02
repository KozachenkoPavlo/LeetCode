from collections import deque
from typing import Optional, List

from data_structures import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            iteration_count = len(queue)
            level_result = []

            while iteration_count > 0:
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                iteration_count -= 1

            result.append(level_result)

        return result
