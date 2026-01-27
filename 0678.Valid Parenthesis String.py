class Solution:
    def checkValidString(self, s: str) -> bool:
        """Dynamic programming interval approach for valid parenthesis with wildcards.

        Intuition:
            Each '*' can be '(', ')' or empty. We can use interval DP where
            dp[i][j] indicates whether substring s[i..j] can form a valid
            sequence of parentheses.

        Approach:
            1. Base case: single '*' characters are valid (as empty string).
            2. For each interval [i, j], check if s[i] and s[j] can form a
               matching pair wrapping a valid inner substring.
            3. Also check if the interval can be split into two valid parts.

        Complexity:
            Time: O(n^3) for the three nested loops
            Space: O(n^2) for the DP table
        """
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for i, char in enumerate(s):
            dp[i][i] = char == "*"
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = (
                    s[i] in "(*" and s[j] in "*)" and (i + 1 == j or dp[i + 1][j - 1])
                )
                dp[i][j] = dp[i][j] or any(
                    dp[i][k] and dp[k + 1][j] for k in range(i, j)
                )
        return dp[0][-1]
