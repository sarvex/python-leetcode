from collections import defaultdict

from sortedcontainers import SortedList


class TweetCounts:
    """Track tweet timestamps and query counts per frequency interval.

    Intuition:
        Store timestamps in sorted order per user to enable efficient range
        counting via binary search.

    Approach:
        Use a SortedList per tweet name for O(log n) insertions and bisect
        queries. For frequency queries, chunk the time range into intervals
        and count tweets in each chunk using bisect_left.

    Complexity:
        Time: O(log n) per record, O(chunks * log n) per query
        Space: O(n) total tweets stored
    """

    def __init__(self) -> None:
        self.interval_seconds = {"minute": 60, "hour": 3600, "day": 86400}
        self.tweets: dict[str, SortedList] = defaultdict(SortedList)

    def recordTweet(self, tweet_name: str, time: int) -> None:
        self.tweets[tweet_name].add(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweet_name: str, start_time: int, end_time: int
    ) -> list[int]:
        interval = self.interval_seconds[freq]
        tweet_times = self.tweets[tweet_name]
        current = start_time
        result: list[int] = []
        while current <= end_time:
            left = tweet_times.bisect_left(current)
            right = tweet_times.bisect_left(min(current + interval, end_time + 1))
            result.append(right - left)
            current += interval
        return result
