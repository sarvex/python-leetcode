class Solution:
    def integerBreak(self, n: int) -> int:
        """Dynamic programming to maximize product of integer parts.

        Intuition:
            For each number i, try all possible first parts j and take the
            maximum of j*(i-j) (no further break) and j*dp[i-j] (further break).

        Approach:
            1. Create a DP array where dp[i] is the maximum product for integer i.
            2. For each i from 2 to n, try all splits j from 1 to i-1.
            3. dp[i] = max(dp[i], j * dp[i-j], j * (i-j)) across all j.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]
