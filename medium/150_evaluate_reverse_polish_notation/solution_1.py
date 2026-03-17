from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    num = stack.pop()
                    stack.append(stack.pop() - num)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    num = stack.pop()
                    stack.append(int(stack.pop() / num))
                case _:
                    stack.append(int(token))

        return stack.pop()
