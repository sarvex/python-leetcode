from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        """
        Compute the minimum operations over all queries to make all elements zero.

        Tagline: Sum half (rounded up) of base-4 digit counts over ranges

        Intuition:
        Each operation divides two chosen numbers by 4 (using floor). For a single
        number x, the required operations to reach 0 equals the number of base-4
        digits of x (smallest k with 4^k > x). Since each operation processes two
        numbers, the minimum operations for a range equals ceil(total_steps / 2),
        where total_steps = sum of base-4 digit counts over that range.

        Approach:
        - Let t(x) be the number of times floor(x/4) must be applied until 0.
          Then t(x) = min k s.t. 4^k > x. For a prefix [1..n],
            sum_{x=1}^n t(x) = sum_{i >= 0} max(0, n - 4^i + 1),
          which we evaluate in O(log_4 n) by iterating powers of 4.
        - For [l..r], total_steps = prefix(r) - prefix(l-1).
        - Minimal operations = ceil(total_steps / 2) = (total_steps + 1) // 2.
        - Sum this minimal count across all queries.

        Complexity:
        - Time: O(q log r_max) with base 4 (≤ 16 iterations per query for r ≤ 1e9)
        - Space: O(1) auxiliary
        """

        def prefix_total_steps(n: int) -> int:
            """Sum of t(x) for x in [1..n] via counting powers of 4.

            - t(x) counts how many thresholds 1, 4, 16, ... are ≤ x.
            """
            if n <= 0:
                return 0

            total = 0
            p = 1  # current power of 4: 4^0, 4^1, ...
            while p <= n:
                total += n - p + 1
                p *= 4
            return total

        total_ops = 0
        for l, r in queries:
            steps = prefix_total_steps(r) - prefix_total_steps(l - 1)
            total_ops += (steps + 1) // 2
        return total_ops
