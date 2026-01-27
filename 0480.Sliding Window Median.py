from collections import defaultdict
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self, window_size: int) -> None:
        self.window_size = window_size
        self.small: list[int] = []
        self.large: list[int] = []
        self.delayed: dict[int, int] = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def add_num(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
            self.small_size += 1
        else:
            heappush(self.large, num)
            self.large_size += 1
        self.rebalance()

    def find_median(self) -> float:
        return (
            -self.small[0]
            if self.window_size & 1
            else (-self.small[0] + self.large[0]) / 2
        )

    def remove_num(self, num: int) -> None:
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.rebalance()

    def prune(self, heap: list[int]) -> None:
        sign = -1 if heap is self.small else 1
        while heap and sign * heap[0] in self.delayed:
            self.delayed[sign * heap[0]] -= 1
            if self.delayed[sign * heap[0]] == 0:
                self.delayed.pop(sign * heap[0])
            heappop(heap)

    def rebalance(self) -> None:
        if self.small_size > self.large_size + 1:
            heappush(self.large, -heappop(self.small))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heappush(self.small, -heappop(self.large))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        """Dual-heap sliding window median with lazy deletion.

        Intuition:
            Maintain two heaps (max-heap for smaller half, min-heap for
            larger half) to efficiently find the median, using lazy deletion
            for the sliding window removal.

        Approach:
            Use a MedianFinder with a small (max) heap and large (min) heap.
            Add elements as the window slides, lazily mark removed elements,
            and prune heaps when their tops are stale. Rebalance heaps to
            keep sizes within one of each other.

        Complexity:
            Time: O(n log n) where n is the length of nums
            Space: O(n) for the heaps and delayed map
        """
        finder = MedianFinder(k)
        for value in nums[:k]:
            finder.add_num(value)
        result = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add_num(nums[i])
            finder.remove_num(nums[i - k])
            result.append(finder.find_median())
        return result
