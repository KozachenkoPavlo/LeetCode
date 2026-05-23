from typing import Optional

from data_structures import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        origin = head
        length = 0

        while head:
            length += 1
            head = head.next

        head = origin
        stack = []

        for _ in range((length + 1) // 2):
            stack.append(head.val)
            head = head.next

        if length % 2 == 1:
            stack.pop()

        while head:
            if head.val != stack.pop():
                return False

            head = head.next

        return True
