import math
from heapq import heappop, heappush


class Solution:
    def mincostToHireWorkers(
        self, quality: list[int], wage: list[int], k: int
    ) -> float:
        """Sort by wage-to-quality ratio and use a max-heap to track cheapest group.

        Intuition:
        When paying workers proportionally to quality, the cost is determined
        by the highest wage/quality ratio in the group. Sorting by this ratio
        and using a heap to maintain the k smallest qualities minimizes cost.

        Approach:
        1. Sort workers by wage/quality ratio
        2. Iterate through sorted workers, maintaining a max-heap of qualities
        3. When heap reaches size k, compute cost as ratio * total quality
        4. Remove the largest quality to make room for potentially cheaper groups

        Complexity:
        Time: O(n log n) for sorting and heap operations
        Space: O(n) for the sorted list and heap
        """
        workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        min_cost = math.inf
        total_quality = 0
        heap: list[int] = []
        for worker_quality, worker_wage in workers:
            total_quality += worker_quality
            heappush(heap, -worker_quality)
            if len(heap) == k:
                min_cost = min(min_cost, worker_wage / worker_quality * total_quality)
                total_quality += heappop(heap)
        return min_cost
