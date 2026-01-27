from bisect import bisect_left


class HitCounter:
    """Hit counter that counts hits in the past 5 minutes (300 seconds)."""

    def __init__(self) -> None:
        """Initialize the hit counter with an empty timestamp list."""
        self.timestamps: list[int] = []

    def hit(self, timestamp: int) -> None:
        """Record a hit at the given timestamp.

        Complexity:
            Time: O(1)
            Space: O(1) amortized
        """
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """Return the number of hits in the past 300 seconds.

        Intuition:
            Since timestamps are monotonically increasing, use binary search
            to find the earliest valid timestamp in the window.

        Approach:
            Use bisect_left to find the index of the first timestamp within
            the 300-second window. The count is total length minus that index.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        return len(self.timestamps) - bisect_left(self.timestamps, timestamp - 300 + 1)
