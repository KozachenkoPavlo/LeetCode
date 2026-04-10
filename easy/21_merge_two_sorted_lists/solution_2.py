from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
