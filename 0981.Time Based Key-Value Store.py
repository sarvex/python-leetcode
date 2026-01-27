from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    """Time-based key-value store using binary search on sorted timestamps.

    Intuition:
    Since timestamps are strictly increasing per key, we can store values in
    order and use binary search to find the latest value at or before a given
    timestamp.

    Approach:
    1. Store (timestamp, value) pairs per key in a defaultdict of lists
    2. For get, binary search for the rightmost timestamp <= query
    3. Return the corresponding value or empty string if none exists

    Complexity:
    Time: O(1) for set, O(log n) for get where n is entries per key
    Space: O(n) total entries stored
    """

    def __init__(self) -> None:
        self.store: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        entries = self.store[key]
        index = bisect_right(entries, (timestamp, chr(127)))
        return entries[index - 1][1] if index else ""
