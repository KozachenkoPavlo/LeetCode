from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time: O(N)
    # Space: O(N)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        result = ListNode()
        saved_link = result

        while stack:
            val = stack.pop()
            result.next = ListNode(val=val)
            result = result.next

        return saved_link.next
