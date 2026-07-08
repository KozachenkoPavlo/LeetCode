from typing import Optional

from data_structures import TreeNode


class Solution:
    # Time: O(N)
    # Space: O(H), where H is a height of a tree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result: Optional[int] = None

        def dfs(node: TreeNode) -> None:
            nonlocal k, result

            if result is not None:
                return

            if node.left:
                dfs(node.left)

            k -= 1
            if k == 0:
                result = node.val
                return

            if node.right:
                dfs(node.right)

        dfs(root)

        if result is not None:
            return result

        raise RuntimeError("K is bigger then the length of the node!")
