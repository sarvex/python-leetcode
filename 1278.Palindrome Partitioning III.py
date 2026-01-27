from math import inf


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """Partition string into k palindromes with minimum changes.

        Intuition:
            Precompute the cost to make any substring a palindrome, then use DP to
            find the minimum total cost of partitioning into exactly k parts.

        Approach:
            Build a cost matrix where cost[i][j] is the number of character changes
            needed to make s[i..j] a palindrome. Then use DP where dp[i][j] represents
            the minimum cost to partition the first i characters into j palindromes.

        Complexity:
            Time: O(n^2 * k)
            Space: O(n^2 + n * k)
        """
        length = len(s)
        cost = [[0] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                cost[i][j] = int(s[i] != s[j])
                if i + 1 < j:
                    cost[i][j] += cost[i + 1][j - 1]

        dp = [[0] * (k + 1) for _ in range(length + 1)]
        for i in range(1, length + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    dp[i][j] = cost[0][i - 1]
                else:
                    dp[i][j] = inf
                    for h in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[h][j - 1] + cost[h][i - 1])
        return dp[length][k]
