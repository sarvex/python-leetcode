from sortedcontainers import SortedList


class ExamRoom:
    """Sorted interval list maintaining maximum-distance seat assignment.

    Intuition:
        Track occupied seats as intervals between adjacent students. The best
        seat maximizes the minimum distance to the nearest student, which
        corresponds to the midpoint of the largest gap.

    Approach:
        1. Maintain a sorted list of intervals keyed by distance (descending)
        2. On seat(): pick the interval with maximum distance, split it
        3. On leave(): merge the two intervals adjacent to the leaving seat
        4. Handle boundary intervals (start/end of room) specially

    Complexity:
        Time: O(log n) per seat/leave operation
        Space: O(n) for storing intervals
    """

    def __init__(self, capacity: int) -> None:
        def distance(interval: tuple[int, int]) -> int:
            left, right = interval
            if left == -1 or right == capacity:
                return right - left - 1
            return (right - left) >> 1

        self.capacity = capacity
        self.intervals: SortedList[tuple[int, int]] = SortedList(
            key=lambda x: (-distance(x), x[0])
        )
        self.left_neighbor: dict[int, int] = {}
        self.right_neighbor: dict[int, int] = {}
        self._add_interval((-1, capacity))

    def seat(self) -> int:
        """Assign the seat that maximizes distance to nearest student."""
        interval = self.intervals[0]
        seat_position = (interval[0] + interval[1]) >> 1
        if interval[0] == -1:
            seat_position = 0
        elif interval[1] == self.capacity:
            seat_position = self.capacity - 1
        self._remove_interval(interval)
        self._add_interval((interval[0], seat_position))
        self._add_interval((seat_position, interval[1]))
        return seat_position

    def leave(self, seat_position: int) -> None:
        """Remove a student and merge adjacent intervals."""
        left = self.left_neighbor[seat_position]
        right = self.right_neighbor[seat_position]
        self._remove_interval((left, seat_position))
        self._remove_interval((seat_position, right))
        self._add_interval((left, right))

    def _add_interval(self, interval: tuple[int, int]) -> None:
        self.intervals.add(interval)
        self.left_neighbor[interval[1]] = interval[0]
        self.right_neighbor[interval[0]] = interval[1]

    def _remove_interval(self, interval: tuple[int, int]) -> None:
        self.intervals.remove(interval)
        self.left_neighbor.pop(interval[1])
        self.right_neighbor.pop(interval[0])
