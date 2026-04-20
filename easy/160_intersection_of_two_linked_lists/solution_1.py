from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N + M), where N is len(headA) and M is len(headB)
    # Space: O(1), we have only two pointers
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        return pointer_a
