import math
from typing import List, Optional

from data_structures import ListNode


class Solution:
    # Time: O(N * K)
    # Space: O(1), because we are not creating a new list, we are reassigning existing
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [node for node in lists if node]

        result = ListNode()
        head = result

        while lists:
            min_node = ListNode(math.inf)
            index_to_move = -1

            for i in range(len(lists)):
                if min_node.val > lists[i].val:
                    min_node = lists[i]
                    index_to_move = i

            head.next = min_node
            head = head.next

            if lists[index_to_move].next is None:
                del lists[index_to_move]
            else:
                lists[index_to_move] = lists[index_to_move].next

        return result.next
