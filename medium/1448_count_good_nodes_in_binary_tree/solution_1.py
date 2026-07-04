from data_structures import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        stack = [(root, root.val)]

        while stack:
            node, prev_max = stack.pop()

            if node.val >= prev_max:
                counter += 1

            if node.left:
                stack.append((node.left, max(prev_max, node.val)))

            if node.right:
                stack.append((node.right, max(prev_max, node.val)))

        return counter
