from typing import List
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Tabulation (bottom-up DP) to find minimum cost to climb stairs.

        Intuition:
            We can either start from the 0th or 1st step and need to reach beyond the last step.
            At each step, we can climb 1 or 2 steps, paying the cost of the current step.

        Approach:
            Use bottom-up dynamic programming to calculate the minimum cost to reach
            each step. We only need to keep track of the last two steps' costs.

        Complexity:
            Time: O(n) where n is the length of the cost array
            Space: O(1) as we only store two variables
        """
        n = len(cost)
        first, second = cost[0], cost[1]

        for i in range(2, n):
            first, second = second, cost[i] + min(first, second)

        return min(first, second)

    def minCostClimbingStairs_memoization(self, cost: List[int]) -> int:
        """Top-down dynamic programming with memoization.

        Intuition:
            We can either start from the 0th or 1st step and need to reach beyond the last step.
            At each step, we can climb 1 or 2 steps, paying the cost of the current step.

        Approach:
            Use top-down dynamic programming (recursion with memoization) to calculate
            the minimum cost to reach the top from each position.

        Complexity:
            Time: O(n) where n is the length of the cost array
            Space: O(n) for the memoization cache
        """
        n = len(cost)

        @cache
        def dp(i: int) -> int:
            return 0 if i >= n else cost[i] + min(dp(i + 1), dp(i + 2))

        return min(dp(0), dp(1))
