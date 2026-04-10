from typing import Optional

from data_structures import ListNode


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
