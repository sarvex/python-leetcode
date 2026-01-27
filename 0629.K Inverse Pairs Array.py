class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """Dynamic programming with prefix sums for counting inverse pairs.

        Intuition:
        Use DP where dp[j] represents the number of arrays of certain length with
        exactly j inverse pairs. Prefix sums allow efficient range sum queries.

        Approach:
        1. Initialize dp array with dp[0] = 1 (one way to have zero inverse pairs).
        2. For each number from 1 to n, update dp using the recurrence with prefix sums.
        3. The prefix sum array enables O(1) range sum lookups instead of inner loops.
        4. Return dp[k] after processing all n numbers.

        Complexity:
        Time: O(n * k)
        Space: O(k)
        """
        mod = 10**9 + 7
        dp = [1] + [0] * k
        prefix = [0] * (k + 2)
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[j] = (prefix[j + 1] - prefix[max(0, j - (i - 1))]) % mod
            for j in range(1, k + 2):
                prefix[j] = (prefix[j - 1] + dp[j - 1]) % mod
        return dp[k]
