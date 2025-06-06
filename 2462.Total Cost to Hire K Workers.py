from typing import List
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """Two-pointer approach with min heaps

        Intuition:
        Use two min heaps to efficiently track candidates from both ends of the array.

        Approach:
        1. Handle edge case where we can just take the k smallest costs
        2. Create two min heaps for first and last 'candidates' workers
        3. Use two pointers to track which workers have been considered
        4. In each of k rounds, pick the worker with minimum cost
        5. Refill the heap from the appropriate side

        Complexity:
        Time: O(n + k log(candidates)) - Building heaps is O(n), k operations with O(log(candidates)) each
        Space: O(candidates) - Two heaps with at most 'candidates' elements each
        """
        n = len(costs)

        # Edge case: if 2*candidates covers all workers, just take k smallest
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])

        # Initialize min heaps for first and last 'candidates' workers
        left_heap = [(costs[i], i) for i in range(candidates)]
        right_heap = [(costs[i], i) for i in range(n - candidates, n)]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        # Initialize pointers for the next workers to consider
        left_ptr, right_ptr = candidates, n - candidates - 1
        total_cost = 0

        def add_worker(heap, is_left):
            nonlocal left_ptr, right_ptr
            if left_ptr <= right_ptr:
                if is_left:
                    heapq.heappush(heap, (costs[left_ptr], left_ptr))
                    left_ptr += 1
                else:
                    heapq.heappush(heap, (costs[right_ptr], right_ptr))
                    right_ptr -= 1

        # Hire k workers
        for _ in range(k):
            # Pick from left heap if it has the cheaper worker or right heap is empty
            if not right_heap or (left_heap and left_heap[0][0] <= right_heap[0][0]):
                cost, _ = heapq.heappop(left_heap)
                total_cost += cost
                add_worker(left_heap, True)
            else:
                cost, _ = heapq.heappop(right_heap)
                total_cost += cost
                add_worker(right_heap, False)

        return total_cost
