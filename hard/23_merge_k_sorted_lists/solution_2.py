import heapq
from typing import List, Optional

from data_structures import ListNode


class Solution:
    # Time: O(N * log K), because taking from a heap takes log(K)
    # Space: O(K), where K is a number of lists, because we need to save it in a heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [node for node in lists if node]

        result = ListNode()
        head = result

        min_heap = []

        for i, node in enumerate(lists):
            heapq.heappush(min_heap, (node.val, i, node))

        while min_heap:
            value, i, node = heapq.heappop(min_heap)
            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return result.next
