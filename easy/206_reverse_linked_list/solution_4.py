from typing import Optional

from data_structures import ListNode


# Bottom-Up Recursion
class Solution:
    # Time: O(N)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
