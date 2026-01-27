class Solution:
    def findDerangement(self, n: int) -> int:
        """Dynamic programming using the derangement recurrence relation.

        Intuition:
        A derangement is a permutation where no element appears in its original
        position. The count follows the recurrence D(n) = (n-1) * (D(n-1) + D(n-2)).

        Approach:
        1. Initialize base cases: D(0) = 1, D(1) = 0.
        2. For each i from 2 to n, compute D(i) = (i-1) * (D(i-1) + D(i-2)) mod 10^9+7.
        3. Return D(n).

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        mod = 10**9 + 7
        dp = [1] + [0] * n
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % mod
        return dp[n]
