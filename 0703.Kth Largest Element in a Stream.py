from heapq import heappop, heappush


class KthLargest:
    """Min-heap of size k to efficiently track the kth largest element.

    Intuition:
        Maintaining a min-heap of exactly k elements ensures the smallest
        element in the heap is always the kth largest overall. New elements
        only enter if they exceed this threshold.

    Approach:
        1. Initialize by adding all elements via the add method.
        2. On each add, push the value onto the heap.
        3. If heap size exceeds k, pop the smallest element.
        4. The heap's root is always the kth largest.

    Complexity:
        Time: O(n log k) for initialization, O(log k) per add
        Space: O(k) for the min-heap
    """

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.min_heap: list[int] = []
        for value in nums:
            self.add(value)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]
