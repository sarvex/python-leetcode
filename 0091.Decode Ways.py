class Solution:
    def numDecodings(self, s: str) -> int:
        """Bottom-Up Dynamic Programming Approach

        Intuition:
            Each character can be decoded alone (if non-zero) or paired with
            the previous character (if the two-digit number is 10-26).

        Approach:
            Use a DP array where dp[i] represents the number of ways to
            decode the first i characters. For each position, add dp[i-1]
            if the current digit is non-zero, and add dp[i-2] if the
            two-digit number formed with the previous digit is valid (10-26).

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        length = len(s)
        dp = [1] + [0] * length
        for i, char in enumerate(s, 1):
            if char != "0":
                dp[i] = dp[i - 1]
            if i > 1 and s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[length]
