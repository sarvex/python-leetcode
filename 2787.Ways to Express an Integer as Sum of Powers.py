class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """Dynamic programming approach to count ways to express n as sum of powers.
        
        Intuition:
        For each number i, we can either include i^x in our sum or exclude it.
        This creates a classic subset sum problem where we need to find ways
        to make sum equal to n using powers of numbers.
        
        Approach:
        Use 2D DP where dp[i][j] represents number of ways to make sum j
        using first i numbers. For each number i, we either:
        1. Don't use i^x: dp[i][j] = dp[i-1][j]
        2. Use i^x: dp[i][j] += dp[i-1][j-i^x] if i^x <= j
        
        Complexity:
        Time: O(n^2) - iterate through n numbers and n possible sums
        Space: O(n^2) - 2D DP table of size (n+1) x (n+1)
        """
        MOD = 10**9 + 7
        
        # dp[i][j] = ways to make sum j using first i numbers
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to make sum 0 with 0 numbers
        
        for i in range(1, n + 1):
            power_value = pow(i, x)
            
            for target_sum in range(n + 1):
                # Don't include current number
                dp[i][target_sum] = dp[i - 1][target_sum]
                
                # Include current number if possible
                if power_value <= target_sum:
                    dp[i][target_sum] = (
                        dp[i][target_sum] + dp[i - 1][target_sum - power_value]
                    ) % MOD
        
        return dp[n][n]
