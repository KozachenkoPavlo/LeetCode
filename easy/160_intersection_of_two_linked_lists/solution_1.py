from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N + M), where N is len(headA) and M is len(headB)
    # Space: O(1), we have only two pointers
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

            if not pointer_a and pointer_b:
                pointer_a = headB

            if not pointer_b and pointer_a:
                pointer_b = headA

        return pointer_a
