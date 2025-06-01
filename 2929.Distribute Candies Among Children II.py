from math import comb


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """Combinatorial approach with inclusion-exclusion principle

        Intuition:
        The problem can be solved using combinations and the inclusion-exclusion principle.
        We start by counting all possible ways to distribute n candies among 3 children,
        then exclude cases where any child exceeds the limit.

        Approach:
        1. If n > 3*limit, it's impossible to distribute candies, so return 0
        2. Count total ways to distribute n candies among 3 children: C(n+2, 2)
        3. Subtract cases where at least one child exceeds the limit
        4. Add back cases where two or more children exceed the limit (to avoid double counting)

        Complexity:
        Time: O(1) - math operations with constant time
        Space: O(1) - only using a constant amount of memory
        """
        # If total candies exceed maximum possible distribution
        if n > 3 * limit:
            return 0

        # Total ways to distribute n candies among 3 children
        total_ways = comb(n + 2, 2)

        # Subtract cases where at least one child exceeds the limit
        if n > limit:
            total_ways -= 3 * comb(n - limit + 1, 2)

        # Add back cases where at least two children exceed the limit
        if n - 2 * limit > 0:
            total_ways += 3 * comb(n - 2 * limit, 2)

        return total_ways
