from heapq import heappop, heappush


class Solution:
    def maxPerformance(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        """Find the maximum performance of a team of at most k engineers.

        Intuition:
            Performance is total_speed * min_efficiency. By sorting engineers
            by efficiency in descending order, each new engineer considered
            sets the minimum efficiency. Use a min-heap to maintain the top-k
            speeds.

        Approach:
            Sort engineers by efficiency descending. Iterate through them,
            adding each speed to a running total and a min-heap. If the heap
            exceeds k, remove the smallest speed. Track the maximum product
            of total speed and current efficiency.

        Complexity:
            Time: O(n log n) for sorting and heap operations.
            Space: O(n)
        """
        engineers = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        max_performance = 0
        speed_sum = 0
        MOD = 10**9 + 7
        min_heap: list[int] = []

        for eng_speed, eng_efficiency in engineers:
            speed_sum += eng_speed
            max_performance = max(max_performance, speed_sum * eng_efficiency)
            heappush(min_heap, eng_speed)
            if len(min_heap) == k:
                speed_sum -= heappop(min_heap)

        return max_performance % MOD
