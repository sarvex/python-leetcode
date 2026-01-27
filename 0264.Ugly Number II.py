from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """Min-heap to generate ugly numbers in ascending order.

        Intuition:
            Starting from 1, each ugly number generates three new candidates by
            multiplying with 2, 3, and 5. A min-heap ensures we always process
            the smallest candidate next.

        Approach:
            1. Initialize a min-heap with 1 and a visited set.
            2. Pop the smallest element n times from the heap.
            3. For each popped value, push its multiples of 2, 3, 5 if not visited.
            4. The nth popped value is the answer.

        Complexity:
            Time: O(n log n) for n heap operations
            Space: O(n) for the heap and visited set
        """
        heap = [1]
        visited = {1}
        current = 1
        for _ in range(n):
            current = heappop(heap)
            for factor in [2, 3, 5]:
                next_ugly = current * factor
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heappush(heap, next_ugly)
        return current
