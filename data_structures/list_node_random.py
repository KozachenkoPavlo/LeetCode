class ListNodeRandom:
    def __init__(
            self, x: int,
            next: 'ListNodeRandom' = None,
            random: 'ListNodeRandom' = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random
