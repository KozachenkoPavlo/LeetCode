from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N + M), N: len(list1), M: len(list2)
    # Space: O(N + M), because stack has to be created for recursion
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
