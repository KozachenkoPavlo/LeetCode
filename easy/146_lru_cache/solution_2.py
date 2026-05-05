class Node:
    def __init__(self, key: int, value: int = 0, prev: "Node" = None, next: "Node" = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.prioritize_node(node)

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.prioritize_node(node)
        else:
            new_node = Node(key, value, prev=self.head, next=self.head.next)
            self.head.next.prev = new_node
            self.head.next = new_node

            self.cache[key] = new_node

            if self.capacity < len(self.cache):
                self.remove_last()

    def prioritize_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head

        node.prev.next = node
        node.next.prev = node

    def remove_last(self):
        del self.cache[self.tail.prev.key]

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
