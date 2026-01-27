class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Dynamic programming to minimize ASCII delete sum of two strings.

        Intuition:
            Similar to longest common subsequence, but instead of maximizing
            match length, we minimize the total ASCII cost of deleted characters.

        Approach:
            1. Build a 2D DP table where dp[i][j] is the minimum delete sum
               for s1[:i] and s2[:j].
            2. Base cases: deleting all of one string when the other is empty.
            3. If characters match, no cost added; otherwise take the minimum
               of deleting from either string.

        Complexity:
            Time: O(m * n) where m, n are lengths of s1, s2
            Space: O(m * n) for the DP table
        """
        length1, length2 = len(s1), len(s2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, length2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1])
                    )
        return dp[length1][length2]
