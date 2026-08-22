import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    # O(F)
    def getNewsFeed(self, userId: int) -> List[int]:
        result = self.posts[userId][-10:]  # O(1)

        for followeeId in self.follows[userId]:  # O(F)
            result.extend(self.posts[followeeId][-10:]) # O(10 * F), only if data reallocation happens

        heapq.heapify(result)  # O(10 * (F + 1))

        return [heapq.heappop(result)[1] for _ in range(min(10, len(result)))]  # O(10 * log(10 * (F + 1))) -> O(log F)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return

        self.follows[followerId].discard(followeeId)
