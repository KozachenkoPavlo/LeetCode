# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_list_node(array: Optional[List]) -> Optional["ListNode"]:
        dummy_node = ListNode()
        node = dummy_node

        for element in array:
            node.next = ListNode(val=element)
            node = node.next

        return dummy_node.next

    @staticmethod
    def list_node_to_list(node: Optional['ListNode']) -> list:
        result = []

        while node:
            result.append(node.val)
            node = node.next

        return result

    def __str__(self) -> str:
        return f"Node({self.val})"

    def __repr__(self):
        return self.__str__()

    def show_list(self) -> str:
        return " -> ".join([str(element) for element in ListNode.list_node_to_list(self)])
