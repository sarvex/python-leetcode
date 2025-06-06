import heapq
from typing import Set


class SmallestInfiniteSet:
    """Min-heap and set approach for efficient smallest number tracking

    Intuition:
        Use a min-heap to efficiently get the smallest number and a set to track
        which numbers have been popped from the infinite set.

    Approach:
        - Track the current smallest number in the infinite set (initially 1)
        - Use a min-heap to store numbers that have been added back
        - Use a set to quickly check if a number is already in our heap

    Complexity:
        Time: O(log n) for both popSmallest and addBack operations
        Space: O(n) where n is the number of elements added back
    """

    def __init__(self):
        self.min_num: int = 1
        self.heap: list[int] = []
        self.num_set: Set[int] = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.num_set.remove(smallest)
            return smallest

        smallest = self.min_num
        self.min_num += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.min_num and num not in self.num_set:
            heapq.heappush(self.heap, num)
            self.num_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
