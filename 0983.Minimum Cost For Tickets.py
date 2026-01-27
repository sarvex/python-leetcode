import math
from bisect import bisect_left
from functools import cache


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        """Top-down DP choosing optimal ticket duration at each travel day.

        Intuition:
        At each travel day, we choose between a 1-day, 7-day, or 30-day pass.
        The optimal choice depends on future travel days, making this a natural
        DP problem with memoization.

        Approach:
        1. For each day index, try all three ticket durations
        2. Binary search to find the next uncovered day after each ticket
        3. Take the minimum cost across all choices
        4. Cache results to avoid recomputation

        Complexity:
        Time: O(n * 3) where n is the number of travel days
        Space: O(n) for memoization cache
        """
        total_days = len(days)
        durations = [1, 7, 30]

        @cache
        def min_cost(index: int) -> int:
            if index >= total_days:
                return 0
            best = math.inf
            for cost, duration in zip(costs, durations):
                next_index = bisect_left(days, days[index] + duration)
                best = min(best, cost + min_cost(next_index))
            return int(best)

        return min_cost(0)
