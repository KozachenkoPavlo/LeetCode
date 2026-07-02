from collections import deque
from typing import Optional, List

from data_structures import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            iteration_count = len(queue)

            while iteration_count > 0:
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                iteration_count -= 1

            result.append(node.val)

        return result
