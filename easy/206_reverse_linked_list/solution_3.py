from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node(val={self.val}, next={self.next})"

# Tail Recursion
class Solution:
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(node: Optional[ListNode], previous: Optional[ListNode] = None) -> Optional[ListNode]:
            if node is None:
                return previous

            next_node = node.next
            node.next = previous

            return recurse(next_node, node)

        result = recurse(head)

        return result
