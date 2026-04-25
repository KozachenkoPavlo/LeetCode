from typing import Optional

from data_structures import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous_slow_pointer = None
        slow_pointer = head
        fast_pointer = head
        distance = 0

        while True:
            if distance == n and not fast_pointer:
                if previous_slow_pointer:
                    previous_slow_pointer.next = slow_pointer.next

                    return head
                else:
                    return slow_pointer.next

            if distance < n and fast_pointer:
                fast_pointer = fast_pointer.next
                distance += 1
            else:
                previous_slow_pointer = slow_pointer
                slow_pointer = slow_pointer.next
                distance -= 1
