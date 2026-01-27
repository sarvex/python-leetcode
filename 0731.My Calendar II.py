from sortedcontainers import SortedDict


class MyCalendarTwo:
    """Sweep line calendar allowing at most double bookings.

    Intuition:
        Use a sweep line approach with event deltas: +1 at start, -1 at end.
        A triple booking occurs when the running sum exceeds 2.

    Approach:
        1. Maintain a SortedDict of time point deltas.
        2. On booking, add +1 at start and -1 at end.
        3. Sweep through all events; if cumulative count exceeds 2, revert
           the booking and return False.
        4. Otherwise return True.

    Complexity:
        Time: O(n) per book where n is the number of bookings
        Space: O(n) for stored events
    """

    def __init__(self) -> None:
        self.events: SortedDict = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        running_count = 0
        for delta in self.events.values():
            running_count += delta
            if running_count > 2:
                self.events[start] -= 1
                self.events[end] += 1
                return False
        return True
