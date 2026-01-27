from bisect import bisect_left
from math import inf


class SnapshotArray:
    """Array supporting snapshots with efficient historical lookups.

    Intuition:
        Instead of copying the entire array on each snapshot, store only
        the changes per index with their snapshot IDs.

    Approach:
        Each index maintains a sorted list of (snap_id, value) pairs. On
        get, use binary search to find the latest value at or before the
        requested snapshot ID.

    Complexity:
        Time: O(1) for set/snap, O(log s) for get where s is the number of sets on that index
        Space: O(total number of set operations)
    """

    def __init__(self, length: int) -> None:
        self.history: list[list[tuple[int, int]]] = [[] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        position = bisect_left(self.history[index], (snap_id, inf)) - 1
        return 0 if position < 0 else self.history[index][position][1]
