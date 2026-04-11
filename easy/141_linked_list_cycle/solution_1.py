from typing import Optional

from data_structures import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next

            if slow.next is not None:
                slow = slow.next

            if slow == fast:
                return True

        return False
