from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        """Greedy approach using min heap to maximize spending

        Intuition:
        To maximize spending, we should buy items in ascending order of their values.
        This way, the more expensive items are bought on later days, multiplying them
        by larger day numbers.

        Approach:
        1. Create a min heap with the last (largest) value from each shop
        2. On each day, buy the cheapest available item
        3. After buying an item, add the next item from the same shop to the heap
        4. Continue until all items are bought

        Complexity:
        Time: O(m*n*log(m)) where m is number of shops and n is items per shop
        Space: O(m) for the priority queue
        """
        # Initialize min heap with the last item from each shop
        pq = [(row[-1], i, len(row) - 1) for i, row in enumerate(values)]
        heapify(pq)

        total_spending = 0
        day = 0

        # Process items in ascending order of value
        while pq:
            day += 1
            value, shop_idx, item_idx = heappop(pq)
            total_spending += value * day

            # Add the next item from the same shop if available
            if item_idx > 0:
                heappush(pq, (values[shop_idx][item_idx - 1], shop_idx, item_idx - 1))

        return total_spending
