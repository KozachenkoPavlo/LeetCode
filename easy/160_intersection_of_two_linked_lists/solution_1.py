from typing import Optional

from data_structures import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        finished_a = False
        pointer_b = headB
        finished_b = False

        while pointer_a and pointer_b:
            if pointer_a == pointer_b:
                return pointer_a

            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

            if pointer_a is None and not finished_a:
                finished_a = True
                pointer_a = headB

            if pointer_b is None and not finished_b:
                finished_b = True
                pointer_b = headA

        return None
