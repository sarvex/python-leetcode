class Logger:
    """Rate-limiting logger that allows messages at most once every 10 seconds."""

    def __init__(self) -> None:
        """Initialize the logger with an empty rate limiter dictionary."""
        self.limiter: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """Check if message should be printed at the given timestamp.

        Intuition:
            Track the next allowed timestamp for each message. If the current
            timestamp is before the allowed time, reject the message.

        Approach:
            Store the earliest allowable timestamp for each message. On each
            call, compare the stored timestamp with the current one. If allowed,
            update the stored timestamp to current + 10.

        Complexity:
            Time: O(1)
            Space: O(n) where n is the number of unique messages
        """
        next_allowed = self.limiter.get(message, 0)
        if next_allowed > timestamp:
            return False
        self.limiter[message] = timestamp + 10
        return True
