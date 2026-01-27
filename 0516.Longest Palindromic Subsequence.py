class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Interval DP to find the longest palindromic subsequence.

        Intuition:
            If characters at both ends match, they extend the palindrome by 2.
            Otherwise, take the best of excluding either end.

        Approach:
            Use a 2D DP table where dp[i][j] is the length of the longest
            palindromic subsequence in s[i..j]. Fill diagonally from single
            characters outward.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for j in range(1, length):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]
