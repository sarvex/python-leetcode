from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """Last Stone Weight using max heap simulation.

        Intuition:
            Always smash the two heaviest stones. A max heap (simulated via
            negation) efficiently retrieves the largest elements.

        Approach:
            Negate all values and heapify. Repeatedly pop the two largest,
            and if they differ, push the difference back. Return the last
            remaining stone or 0.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        heap = [-weight for weight in stones]
        heapify(heap)
        while len(heap) > 1:
            heaviest, second = -heappop(heap), -heappop(heap)
            if second != heaviest:
                heappush(heap, second - heaviest)
        return 0 if not heap else -heap[0]
