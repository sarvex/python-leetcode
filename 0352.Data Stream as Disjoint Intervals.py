from sortedcontainers import SortedDict


class SummaryRanges:
    """Maintains disjoint intervals from a stream of integers.

    Intuition:
        A sorted mapping from interval starts to interval bounds allows
        efficient lookup of neighboring intervals when a new value arrives,
        enabling O(log n) merging.

    Approach:
        Use a SortedDict keyed by interval start. On addNum, binary search
        for the insertion point to find left and right neighbor intervals.
        Merge with neighbors if the new value is adjacent or overlapping,
        otherwise create a new singleton interval.

    Complexity:
        Time: O(log n) per addNum, O(n) per getIntervals
        Space: O(n) for storing all intervals
    """

    def __init__(self) -> None:
        """Initialize the interval store."""
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        """Add an integer to the data stream and merge intervals as needed."""
        num_intervals = len(self.intervals)
        right_idx = self.intervals.bisect_right(val)
        left_idx = num_intervals if right_idx == 0 else right_idx - 1
        keys = self.intervals.keys()
        values = self.intervals.values()
        if (
            left_idx != num_intervals
            and right_idx != num_intervals
            and values[left_idx][1] + 1 == val
            and values[right_idx][0] - 1 == val
        ):
            self.intervals[keys[left_idx]][1] = self.intervals[keys[right_idx]][1]
            self.intervals.pop(keys[right_idx])
        elif left_idx != num_intervals and val <= values[left_idx][1] + 1:
            self.intervals[keys[left_idx]][1] = max(
                val, self.intervals[keys[left_idx]][1]
            )
        elif right_idx != num_intervals and val >= values[right_idx][0] - 1:
            self.intervals[keys[right_idx]][0] = min(
                val, self.intervals[keys[right_idx]][0]
            )
        else:
            self.intervals[val] = [val, val]

    def getIntervals(self) -> list[list[int]]:
        """Return the current set of disjoint intervals sorted by start."""
        return list(self.intervals.values())
