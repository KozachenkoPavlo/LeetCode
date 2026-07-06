from typing import Optional

from data_structures import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)

            array.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)

        return array[k - 1]
