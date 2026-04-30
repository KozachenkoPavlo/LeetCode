from typing import Optional

from data_structures import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        ref = result

        left = 0

        while l1 is not None or l2 is not None or left != 0:
            num_1 = l1.val if l1 else 0
            num_2 = l2.val if l2 else 0

            num_sum = num_1 + num_2 + left
            left = num_sum // 10

            ref.next = ListNode(num_sum % 10)
            ref = ref.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
