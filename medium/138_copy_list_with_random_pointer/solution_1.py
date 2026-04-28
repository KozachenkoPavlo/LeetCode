from typing import Optional

from data_structures import ListNodeRandom as Node


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        root = head
        new_list = Node(0)
        result = new_list

        # Copy without random link
        while head:
            new_list.next = Node(head.val)
            new_list = new_list.next
            head = head.next

        head = root
        new_list = result.next

        while head is not None:
            if head.random is None:
                head = head.next
                new_list = new_list.next

                continue

            nodes_to_search = root
            counter = 0

            while nodes_to_search:
                if nodes_to_search == head.random:
                    break

                counter += 1
                nodes_to_search = nodes_to_search.next

            rand_node = result.next

            while counter > 0:
                rand_node = rand_node.next
                counter -= 1

            new_list.random = rand_node

            head = head.next
            new_list = new_list.next

        return result.next
