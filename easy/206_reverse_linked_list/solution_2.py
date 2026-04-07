from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node(val={self.val}, next={self.next})"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        next_node = current.next if current else None

        while current:
            current.next = previous
            previous = current
            current = next_node
            next_node = current.next if current else None

        return previous
