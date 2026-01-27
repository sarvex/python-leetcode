import math
from functools import cache


class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        """Memoized DFS exploring rod placement for two equal-height supports.

        Intuition:
            Each rod can go on the left support, right support, or be skipped.
            Track the height difference between supports; when difference is 0,
            we have equal supports.

        Approach:
            1. Define DFS(index, diff) = max achievable height for the shorter support.
            2. For each rod, try: skip it, add to taller side, or add to shorter side.
            3. Base case: if all rods processed, return 0 if diff == 0, else -infinity.
            4. Use memoization to avoid recomputation.

        Complexity:
            Time: O(n * S) — n rods, S = sum of all rod lengths
            Space: O(n * S) — memoization cache
        """

        @cache
        def dfs(index: int, difference: int) -> int:
            if index >= len(rods):
                return 0 if difference == 0 else -math.inf
            result = max(
                dfs(index + 1, difference), dfs(index + 1, difference + rods[index])
            )
            result = max(
                result,
                dfs(index + 1, abs(rods[index] - difference))
                + min(difference, rods[index]),
            )
            return result

        return dfs(0, 0)
