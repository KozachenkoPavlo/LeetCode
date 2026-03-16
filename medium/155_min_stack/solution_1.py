# Space: O(2 * n) -> O()
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Time: O(1)
    def push(self, val: int) -> None:
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

        self.stack.append(val)

    # Time: O(1)
    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    # Time: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Time: O(1)
    def getMin(self) -> int:
        return self.min_stack[-1]
