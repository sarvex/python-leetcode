from collections import defaultdict
from heapq import heappop, heappush


class FreqStack:
    """Max-heap frequency stack using frequency and timestamp ordering.

    Intuition:
        To pop the most frequent element (with recency as tiebreaker),
        maintain a max-heap keyed by (-frequency, -timestamp, value).

    Approach:
        1. Track each value's frequency in a counter.
        2. On push, increment frequency and timestamp, then push to the heap.
        3. On pop, extract the top element (highest frequency, most recent)
           and decrement its frequency.

    Complexity:
        Time: O(log n) per push/pop operation.
        Space: O(n)
    """

    def __init__(self) -> None:
        self.frequency: dict[int, int] = defaultdict(int)
        self.heap: list[tuple[int, int, int]] = []
        self.timestamp: int = 0

    def push(self, val: int) -> None:
        self.timestamp += 1
        self.frequency[val] += 1
        heappush(self.heap, (-self.frequency[val], -self.timestamp, val))

    def pop(self) -> int:
        val = heappop(self.heap)[2]
        self.frequency[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
