class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Find minimum delete operations to make two strings equal using DP.

        Intuition:
            This is equivalent to finding the longest common subsequence and
            then deleting all non-LCS characters from both strings.

        Approach:
            1. Build a 2D DP table where dp[i][j] represents minimum deletions
               for word1[:i] and word2[:j].
            2. Base cases: dp[i][0] = i and dp[0][j] = j (delete all chars).
            3. If characters match, no deletion needed (take diagonal value).
            4. Otherwise, take minimum of deleting from either string plus one.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(word1), len(word2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            dp[i][0] = i
        for j in range(1, cols + 1):
            dp[0][j] = j
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
