from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self.calls = deque()

    """
    Sliding window with queue implementation

    Intuition:
    Keep track of recent calls within a sliding window of 3000 milliseconds.
    Older calls outside this window are no longer needed and can be removed.

    Approach:
    Use a queue to maintain calls in chronological order.
    For each new call, remove older calls that fall outside the 3000ms window.

    Complexity:
    - Time: O(1) amortized for each ping operation
    - Space: O(n) where n is the number of calls within a 3000ms window
    """
    def ping(self, t: int) -> int:
        self.calls.append(t)

        # Remove calls outside the 3000ms window
        while self.calls and self.calls[0] < t - 3000:
            self.calls.popleft()

        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
