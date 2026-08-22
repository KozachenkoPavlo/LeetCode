import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timestamp = 1
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        for post in self.posts.get(userId, [])[-10:]:
            heapq.heappush(result, (-post[0], post[1]))

        for followId in self.follows.get(userId, set()):
            for post in self.posts.get(followId, [])[-10:]:
                heapq.heappush(result, (-post[0], post[1]))

        return [heapq.heappop(result)[1] for _ in range(min(10, len(result)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return

        self.follows[followerId].discard(followeeId)
