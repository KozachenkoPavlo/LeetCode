from solution_1 import Solution, ListNode

if __name__ == "__main__":
    s = Solution()
    tests = [
        ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    ]

    for test in tests:
        result = s.reverseList(test)
        print(result)
