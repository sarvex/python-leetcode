from functools import cache
from math import inf


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        """Build minimum cost tree from leaf values using interval DP.

        Intuition:
            For each way to split a subarray, the cost is the product of the
            max values of left and right subtrees plus their respective costs.

        Approach:
            Use memoized DFS over intervals [i, j]. For each split point k,
            compute sum of subtree costs plus product of max leaf values.
            Return minimum total cost and corresponding max leaf value.

        Complexity:
            Time: O(n^3) for all intervals and split points
            Space: O(n^2) for memoization cache
        """

        @cache
        def dfs(left: int, right: int) -> tuple[int, int]:
            if left == right:
                return 0, arr[left]
            min_cost, max_leaf = inf, -1
            for mid in range(left, right):
                cost_left, max_left = dfs(left, mid)
                cost_right, max_right = dfs(mid + 1, right)
                total = cost_left + cost_right + max_left * max_right
                if min_cost > total:
                    min_cost = total
                    max_leaf = max(max_left, max_right)
            return min_cost, max_leaf

        return dfs(0, len(arr) - 1)[0]
