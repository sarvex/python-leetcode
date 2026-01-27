class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        """Compute probability of getting exactly target heads from biased coins.

        Intuition:
            Each coin contributes independently, so we can build up the
            probability of reaching exactly j heads after tossing i coins
            using dynamic programming.

        Approach:
            Use a 2D DP table where dp[i][j] is the probability of j heads
            after tossing the first i coins. Transition considers whether
            coin i lands heads (probability p) or tails (probability 1-p).

        Complexity:
            Time: O(n * target)
            Space: O(n * target)
        """
        coin_count = len(prob)
        dp = [[0.0] * (target + 1) for _ in range(coin_count + 1)]
        dp[0][0] = 1.0
        for i, p in enumerate(prob, 1):
            for j in range(min(i, target) + 1):
                dp[i][j] = (1 - p) * dp[i - 1][j]
                if j:
                    dp[i][j] += p * dp[i - 1][j - 1]
        return dp[coin_count][target]
