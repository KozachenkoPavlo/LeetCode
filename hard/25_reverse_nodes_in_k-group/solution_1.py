from typing import Optional

from data_structures import ListNode


class Solution:
    def get_kth_element(self, node: ListNode, k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1

        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev_tail = dummy

        while True:
            group_curr_tail = self.get_kth_element(group_prev_tail, k)

            if not group_curr_tail:
                break

            group_next_head = group_curr_tail.next

            # Reversing the list
            previous, current = group_curr_tail.next, group_prev_tail.next
            while current != group_next_head:
                temporary = current.next
                current.next = previous
                previous = current
                current = temporary

            temporary = group_prev_tail.next
            group_prev_tail.next = previous
            group_prev_tail = temporary

        return dummy.next
