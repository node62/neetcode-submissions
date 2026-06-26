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
        people = self.following[userId] | set([userId])

        heap = []
        
        # fill heap with last elements
        for p in people:
            if len(self.user_tweets[p]) > 0:
                time, tweetId = self.user_tweets[p][-1]
                idx = len(self.user_tweets[p]) - 1

                heappush_max(heap, (time, tweetId, p, idx))
        
        # get top 10
        ans = []
        i = 0
        while heap and i < 10:
            _, top_tweetId, p, idx = heappop_max(heap)
            ans.append(top_tweetId)

            if idx - 1 >= 0:
                time, tweetId = self.user_tweets[p][idx - 1]
                heappush_max(heap, (time, tweetId, p, idx - 1))
            
            i += 1
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
