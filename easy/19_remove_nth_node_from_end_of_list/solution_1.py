from typing import Optional

from data_structures import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None

            next_node = helper(node.next)
            node.next = next_node

            nonlocal counter
            counter += 1

            if counter == n:
                return next_node
            else:
                return node

        counter = 0

        return helper(head)
