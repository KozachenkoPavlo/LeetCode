from typing import Optional

from data_structures import ListNode


class Solution:
    # Time: O(N + M), N: len(list1), M: len(list2)
    # Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        result = list1
        previous = None

        while list2:
            if list1.val > list2.val:
                keep_link = list2.next

                if previous is None:
                    list2.next = list1
                    list1 = list2
                    result = list1
                else:
                    previous.next = list2
                    previous = previous.next
                    list2.next = list1

                list2 = keep_link
            elif list1.val <= list2.val:
                if list1.next is None:
                    list1.next = list2
                else:
                    previous = list1
                    list1 = list1.next

        return result
