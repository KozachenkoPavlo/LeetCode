from typing import Optional

from data_structures import ListNodeRandom as Node


class Solution:
    # Time: O(N)
    # Space: O(N)
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        root = head
        new_list = Node(0)
        result = new_list
        registry = {None: None}

        while head:
            new_list.next = Node(head.val)
            registry[head] = new_list.next

            new_list = new_list.next
            head = head.next

        head = root
        new_list = result.next

        while head:
            new_list.random = registry[head.random]

            head = head.next
            new_list = new_list.next

        return result.next
