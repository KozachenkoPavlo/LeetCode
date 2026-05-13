from typing import Optional

from data_structures import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                return slow

            slow = slow.next

        return slow
