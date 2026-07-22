class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def __sync(self):
        if self.stack_out:
            return

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())


    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.__sync()

        return self.stack_out.pop()

    def peek(self) -> int:
        self.__sync()

        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
