from heapq import heappop, heappush, heappushpop


class MedianFinder:
    """Maintains a running median using two heaps.

    Intuition:
        The median splits the data into two halves. By keeping the smaller
        half in a max-heap and the larger half in a min-heap, the median
        is always accessible at the tops of the heaps.

    Approach:
        Use a negated min-heap to simulate a max-heap for the smaller half.
        On each insertion, push to the max-heap first, then move the max
        element to the min-heap. Rebalance if the min-heap grows more than
        one element larger than the max-heap. The median is either the top
        of the min-heap (odd count) or the average of both tops (even count).

    Complexity:
        Time: O(log n) per addNum, O(1) per findMedian
        Space: O(n) for storing all elements across two heaps
    """

    def __init__(self) -> None:
        """Initialize with empty heaps for the smaller and larger halves."""
        self.min_heap: list[int] = []
        self.max_heap: list[int] = []

    def addNum(self, num: int) -> None:
        """Add a number to the data structure, rebalancing heaps as needed."""
        heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        """Return the median of all numbers added so far."""
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]
