from typing import Optional

from data_structures import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        result = ListNode()
        head = result
        remember = False

        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            save_val = val1 + val2
            save_val += 1 if remember else 0
            remember = save_val > 9

            head.next = ListNode(val=save_val % 10)

            head = head.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if remember:
            head.next = ListNode(val=1)

        return result.next
