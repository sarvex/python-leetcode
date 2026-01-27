from collections import defaultdict
from heapq import nlargest


class Twitter:
    """Simplified Twitter with post, follow, unfollow, and news feed.

    Intuition:
        Each user maintains a list of tweets and a set of followees. The news
        feed is assembled by collecting recent tweets from the user and all
        followees, then selecting the most recent ones.

    Approach:
        Track tweets per user with timestamps for chronological ordering.
        Maintain follow relationships using sets. For getNewsFeed, gather
        the 10 most recent tweets from each relevant user and use nlargest
        to pick the overall top 10 by timestamp.

    Complexity:
        Time: O(1) for post/follow/unfollow, O(f) for getNewsFeed where f
              is the number of followees
        Space: O(t + u) where t is total tweets and u is total users
    """

    def __init__(self) -> None:
        """Initialize the Twitter data structures."""
        self.user_tweets: dict[int, list[int]] = defaultdict(list)
        self.user_following: dict[int, set[int]] = defaultdict(set)
        self.tweet_time: dict[int, int] = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Post a new tweet for the given user."""
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweet_time[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> list[int]:
        """Retrieve the 10 most recent tweets from the user and their followees."""
        following = self.user_following[userId]
        users = set(following)
        users.add(userId)
        tweets = [self.user_tweets[user][::-1][:10] for user in users]
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key=lambda tweet: self.tweet_time[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        """Make followerId follow followeeId."""
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Make followerId unfollow followeeId."""
        following = self.user_following[followerId]
        if followeeId in following:
            following.remove(followeeId)
