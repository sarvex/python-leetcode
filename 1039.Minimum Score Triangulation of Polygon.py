from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        Bottom-up DP for minimum polygon triangulation score.

        Intuition:
        - Triangulating a convex polygon can be decomposed: pick a last triangle (i, k, j),
          then optimally triangulate the two sub-polygons (i..k) and (k..j).

        Approach:
        - Let `dp[i][j]` be the minimum score to triangulate the sub-polygon from i to j (inclusive).
        - Iterate by sub-polygon length L = 3..n, and for each pair (i, j), try all k in (i, j).
        - Transition: dp[i][j] = min(dp[i][k] + dp[k][j] + values[i]*values[k]*values[j]).

        Complexity:
        - Time: O(N^3)
        - Space: O(N^2)
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for L in range(3, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1
                best = float("inf")
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best

        return dp[0][n - 1]
