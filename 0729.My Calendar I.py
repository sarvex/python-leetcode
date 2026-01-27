from sortedcontainers import SortedDict


class MyCalendar:
    """Sorted dictionary based calendar for non-overlapping bookings.

    Intuition:
        Store intervals keyed by end time with start time as value. Use binary
        search to efficiently check for overlaps before inserting.

    Approach:
        1. Maintain a SortedDict mapping end -> start for booked intervals.
        2. On booking [start, end), find the first interval ending after start.
        3. If that interval's start is before our end, there's an overlap.
        4. Otherwise, insert the new interval.

    Complexity:
        Time: O(log n) per book operation
        Space: O(n) for stored intervals
    """

    def __init__(self) -> None:
        self.sorted_intervals: SortedDict = SortedDict()

    def book(self, start: int, end: int) -> bool:
        idx = self.sorted_intervals.bisect_right(start)
        if (
            idx < len(self.sorted_intervals)
            and end > self.sorted_intervals.values()[idx]
        ):
            return False
        self.sorted_intervals[end] = start
        return True
