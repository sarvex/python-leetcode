from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        """
        Two-heap approach for maximizing capital with limited project selection.

        Intuition:
        Use min-heap for available projects and max-heap for profitable projects.
        At each step, select the most profitable project among available ones.

        Approach:
        1. Create a min-heap of (capital, profit) pairs
        2. Maintain a max-heap for available projects (profits)
        3. For each of k projects:
           - Move all affordable projects to max-heap
           - Select the most profitable project
           - Update current capital

        Complexity:
        Time: O(n log n), where n is the number of projects
        Space: O(n) for the two heaps
        """
        # Create min-heap of (capital, profit) pairs
        projects = list(zip(capital, profits))
        heapify(projects)

        # Max-heap for available projects (using negative values for max-heap)
        available = []

        # Select up to k projects
        for _ in range(k):
            # Move all affordable projects to the available heap
            while projects and projects[0][0] <= w:
                c, p = heappop(projects)
                heappush(available, -p)  # Negate for max-heap

            # If no projects are available, we're done
            if not available:
                break

            # Select the most profitable project and update capital
            w += -heappop(available)  # Negate back to get positive profit

        return w
