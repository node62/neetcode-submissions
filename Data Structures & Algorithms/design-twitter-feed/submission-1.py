from heapq import *
class Twitter:  

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:        
        self.user_tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.user_tweets[userId][:]
        for f in self.following[userId]:
            arr = self.user_tweets[f]
            heap = heap + arr
        heapify(heap)
        ans = nlargest(10, heap)        
        return [v for k, v in ans]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
