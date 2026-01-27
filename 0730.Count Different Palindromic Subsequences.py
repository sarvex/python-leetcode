class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """3D DP counting distinct palindromic subsequences by boundary character.

        Intuition:
            Track palindromic subsequences by their outermost character. For each
            substring and each character in 'abcd', count distinct palindromic
            subsequences bounded by that character.

        Approach:
            1. dp[i][j][c] = number of distinct palindromic subsequences in
               s[i..j] that are bounded by character c.
            2. If s[i] == s[j] == c, count includes the pair plus all inner
               palindromes (2 + sum of all inner counts).
            3. If only one end matches c, inherit from the subproblem excluding
               the non-matching end.
            4. Sum all characters at dp[0][n-1] for the final answer.

        Complexity:
            Time: O(n^2 * 4) where n is the length of s
            Space: O(n^2 * 4) for the DP table
        """
        MOD = 10**9 + 7
        length = len(s)
        dp = [[[0] * 4 for _ in range(length)] for _ in range(length)]
        for i, char in enumerate(s):
            dp[i][i][ord(char) - ord("a")] = 1
        for span in range(2, length + 1):
            for i in range(length - span + 1):
                j = i + span - 1
                for char in "abcd":
                    char_idx = ord(char) - ord("a")
                    if s[i] == s[j] == char:
                        dp[i][j][char_idx] = 2 + sum(dp[i + 1][j - 1])
                    elif s[i] == char:
                        dp[i][j][char_idx] = dp[i][j - 1][char_idx]
                    elif s[j] == char:
                        dp[i][j][char_idx] = dp[i + 1][j][char_idx]
                    else:
                        dp[i][j][char_idx] = dp[i + 1][j - 1][char_idx]
        return sum(dp[0][-1]) % MOD
