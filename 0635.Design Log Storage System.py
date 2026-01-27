class LogSystem:
    """Log storage system with granularity-based timestamp retrieval.

    Intuition:
    Timestamps are strings with fixed format. By truncating to the appropriate
    prefix length based on granularity, we can compare timestamps at any level.

    Approach:
    1. Store logs as (id, timestamp) pairs.
    2. Map each granularity to a prefix length for comparison.
    3. On retrieve, filter logs whose truncated timestamp falls within the range.

    Complexity:
    Time: O(n) per retrieve, O(1) per put
    Space: O(n)
    """

    def __init__(self) -> None:
        self.logs: list[tuple[int, str]] = []
        self.granularity_length = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        prefix_len = self.granularity_length[granularity]
        return [
            id
            for id, ts in self.logs
            if start[:prefix_len] <= ts[:prefix_len] <= end[:prefix_len]
        ]
