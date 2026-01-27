from itertools import accumulate
from math import inf


class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        """Find minimum cost to merge all stones into one pile.

        Intuition:
            Each merge reduces the pile count by k-1, so merging is only possible
            when (n-1) % (k-1) == 0. Use interval DP with a third dimension for
            the number of resulting piles.

        Approach:
            Let f[i][j][p] = minimum cost to merge stones[i..j] into p piles.
            Transition: split at some midpoint h into 1 pile and (p-1) piles.
            Merging p=k piles into 1 adds the range sum cost.

        Complexity:
            Time: O(n^3 * k) for the three nested loops plus split point
            Space: O(n^2 * k) for the DP table
        """
        length = len(stones)
        if (length - 1) % (k - 1):
            return -1
        prefix_sum = list(accumulate(stones, initial=0))
        dp = [[[inf] * (k + 1) for _ in range(length + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            dp[i][i][1] = 0
        for span in range(2, length + 1):
            for i in range(1, length - span + 2):
                j = i + span - 1
                for piles in range(1, k + 1):
                    for mid in range(i, j):
                        dp[i][j][piles] = min(
                            dp[i][j][piles],
                            dp[i][mid][1] + dp[mid + 1][j][piles - 1],
                        )
                dp[i][j][1] = dp[i][j][k] + prefix_sum[j] - prefix_sum[i - 1]
        return dp[1][length][1]
