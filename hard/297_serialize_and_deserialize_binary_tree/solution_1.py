from collections import deque
from typing import Optional

from data_structures import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is not None:
                result.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")

        return " ".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        queue = deque(data.split())
        root = TreeNode(val=int(queue.popleft()))
        nodes = deque([root])

        while queue:
            nodes_to_process = nodes.copy()
            nodes.clear()

            for node in nodes_to_process:
                left_value = queue.popleft()
                if left_value != "None":
                    node.left = TreeNode(int(left_value))
                    nodes.append(node.left)

                right_value = queue.popleft()
                if right_value != "None":
                    node.right = TreeNode(int(right_value))
                    nodes.append(node.right)

        return root
