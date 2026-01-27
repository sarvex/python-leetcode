from functools import cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """Memoized DFS decomposing target using powers of x.

        Intuition:
            Express the target as a sum/difference of powers of x. For each value,
            find the nearest power of x and decide whether to approach from below
            or above, minimizing total operators.

        Approach:
            1. Base case: if x >= value, use x/x repeated (cost 2*value-1) or
               subtraction from x (cost 2*(x-value)).
            2. Find smallest power k where x^k >= value.
            3. Try expressing as x^k - remainder (approach from above).
            4. Try expressing as remainder after x^(k-1) (approach from below).
            5. Return minimum cost path.

        Complexity:
            Time: O(target * log_x(target)) — bounded by memoized states
            Space: O(target) — memoization cache
        """

        @cache
        def dfs(value: int) -> int:
            if x >= value:
                return min(value * 2 - 1, 2 * (x - value))
            power = 2
            while x**power < value:
                power += 1
            if x**power - value < value:
                return min(
                    power + dfs(x**power - value),
                    power - 1 + dfs(value - x ** (power - 1)),
                )
            return power - 1 + dfs(value - x ** (power - 1))

        return dfs(target)
