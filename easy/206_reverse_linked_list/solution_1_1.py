from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head
        previous = None

        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        return previous
