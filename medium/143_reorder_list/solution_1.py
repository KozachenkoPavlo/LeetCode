from typing import Optional

from data_structures import ListNode


class Solution:
    def convert_list_to_list_node(self, array: list) -> Optional[ListNode]:
        head = ListNode()
        node = head

        for element in array:
            node.next = ListNode(element)
            node = node.next

        return head.next

    def reverse(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head

        reversed_list = self.reverse(head.next)

        next_node = head.next
        next_node.next = head
        head.next = None

        return reversed_list

    def get_list_node_len(self, head: Optional[ListNode]) -> int:
        length = 0

        while head:
            head = head.next
            length += 1

        return length

    def split_list(self, head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if not head:
            return head, head

        if not head.next:
            return head, head.next

        length = self.get_list_node_len(head)
        index = 0

        left_part = ListNode()
        origin_left = left_part

        while index < (length + 1) // 2:
            left_part.next = head
            left_part = left_part.next

            head = head.next
            index += 1

        if left_part:
            left_part.next = None

        return origin_left.next, head

    def show_list(self, head: Optional[ListNode]) -> None:
        while head:
            print(f"{head.val} -> ", end="")
            head = head.next

        print("None")

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = list1

        while list1 and list2:
            keep_node = list1.next
            list1.next = list2
            list2 = list2.next

            list1.next.next = keep_node
            list1 = list1.next.next

        return result

    # Time: O(3N)
    # Space: O(N), because of stack in recursion
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left, right = self.split_list(head)

        self.merge_lists(left, self.reverse(right))


if __name__ == "__main__":
    tests = [
        [1, 2, 3, 4],
        [],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]
    s = Solution()

    for index in range(len(tests)):
        tests[index] = s.convert_list_to_list_node(tests[index])

    for test in tests:
        s.show_list(test)
        print(f"Length: {s.get_list_node_len(test)}")
        left, right = s.split_list(test)
        print("Left: ", end="")
        s.show_list(left)
        print("Right: ", end="")
        s.show_list(right)
        print("Merged list: ", end="")
        s.show_list(s.merge_lists(left, s.reverse(right)))
        print("\n\n\n")
