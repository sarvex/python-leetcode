class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """Valid palindrome III using longest palindromic subsequence.

        Intuition:
            A string is a valid palindrome with at most k removals if its longest
            palindromic subsequence length plus k is at least the string length.

        Approach:
            Use dynamic programming to compute the longest palindromic subsequence.
            f[i][j] stores the LPS length for substring s[i..j]. Early return
            when f[i][j] + k >= n.

        Complexity:
            Time: O(n^2) where n is the length of the string
            Space: O(n^2) for the DP table
        """
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if dp[i][j] + k >= length:
                    return True
        return False
