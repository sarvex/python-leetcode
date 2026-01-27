class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """Last Stone Weight II via 0/1 knapsack subset sum.

        Intuition:
            This reduces to partitioning stones into two groups to minimize
            the absolute difference, which is a 0/1 knapsack problem targeting
            half the total sum.

        Approach:
            Compute the total sum. Use DP where dp[i][j] is the maximum
            weight achievable using the first i stones with capacity j.
            The answer is total_sum - 2 * dp[m][half].

        Complexity:
            Time: O(m * S) where S is half the total sum
            Space: O(m * S)
        """
        total_sum = sum(stones)
        stone_count, half = len(stones), total_sum >> 1
        dp = [[0] * (half + 1) for _ in range(stone_count + 1)]
        for i in range(1, stone_count + 1):
            for j in range(half + 1):
                dp[i][j] = dp[i - 1][j]
                if stones[i - 1] <= j:
                    dp[i][j] = max(
                        dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1]
                    )
        return total_sum - 2 * dp[-1][-1]
