from typing import List, Optional

from data_structures import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_value = preorder[0]
        split_index = inorder.index(root_value)

        root = TreeNode(
            val=root_value,
            left=self.buildTree(
                preorder[1:split_index + 1],
                inorder[:split_index],
            ),
            right=self.buildTree(
                preorder[split_index + 1:],
                inorder[split_index + 1:],
            )
        )

        return root


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4], [2, 1, 3, 4])
    ]
    s = Solution()

    for test in tests:
        print(s.buildTree(*test))
