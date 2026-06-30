from data_structures import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


if __name__ == "__main__":
    tests = [
        {"args": [
            TreeNode(5,
                     TreeNode(3,
                              TreeNode(1,
                                       None,
                                       TreeNode(2)),
                              TreeNode(4)),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9))),
            TreeNode(3), TreeNode(8)],
            "expected": 5
        },
        {"args": [
            TreeNode(5,
                     TreeNode(3,
                              TreeNode(1,
                                       None,
                                       TreeNode(2)),
                              TreeNode(4)),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9))),
            TreeNode(3), TreeNode(4)],
            "expected": 3
        }
    ]

    s = Solution()

    for test in tests:
        args = test["args"]
        expected = test["expected"]

        result = s.lowestCommonAncestor(*args)

        if result.val == expected:
            print("PASSED!")
        else:
            print(f"Expected: {expected}, given: {result}")
