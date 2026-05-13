from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N), the list will be gone through 1.5 times
    # Space: O(1), only two pointers
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
