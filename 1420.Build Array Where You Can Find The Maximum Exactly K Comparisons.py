class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """Count arrays of length n with max value m and search cost k.

        Intuition:
            Use 3D DP where state is (array length, search cost, current max).
            A new maximum increments the search cost.

        Approach:
            dp[i][c][j] = number of arrays of length i with search cost c
            and current maximum j. For each position, either reuse a value
            <= current max (no cost increase) or set a new max (cost + 1).

        Complexity:
            Time: O(n * k * m^2) for filling the DP table
            Space: O(n * k * m) for the DP array
        """
        if k == 0:
            return 0
        modulus = 10**9 + 7
        dp = [[[0] * (m + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        for max_val in range(1, m + 1):
            dp[1][1][max_val] = 1
        for length in range(2, n + 1):
            for cost in range(1, min(k + 1, length + 1)):
                for max_val in range(1, m + 1):
                    dp[length][cost][max_val] = dp[length - 1][cost][max_val] * max_val
                    for prev_max in range(1, max_val):
                        dp[length][cost][max_val] += dp[length - 1][cost - 1][prev_max]
                        dp[length][cost][max_val] %= modulus
        result = 0
        for max_val in range(1, m + 1):
            result += dp[n][k][max_val]
            result %= modulus
        return result
