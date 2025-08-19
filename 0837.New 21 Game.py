class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Tagline: Sliding-window DP for probability accumulation

        Intuition:
            Model the game as reaching final totals in [0..n]. While points < k,
            we continue drawing; when points >= k, we stop. We need the
            probability mass that lands in [k..n].

        Approach:
            Use bottom-up DP with a moving window sum.
            Let dp[i] be the probability of landing exactly on total i.
            For i > 0, dp[i] = (dp[i-1] + ... + dp[i-maxPts]) / maxPts,
            but only predecessors with index < k contribute to the window,
            because we stop drawing once we reach >= k.
            Maintain a running wsum of the last maxPts valid dp values to get
            O(1) transition per i. Early-return for trivial full-probability cases.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        # Early exits
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp: list[float] = [0.0] * (n + 1)
        dp[0] = 1.0
        wsum = 1.0  # sum of last maxPts dp values that are from indices < k
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = wsum / maxPts
            if i < k:
                wsum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                wsum -= dp[i - maxPts]

        return result
