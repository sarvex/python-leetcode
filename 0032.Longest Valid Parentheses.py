class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Dynamic Programming approach to find longest valid parentheses substring

        Intuition:
        Use dynamic programming to track the length of valid parentheses ending at each position.
        When we encounter a closing parenthesis, we check if it forms a valid pair with a previous
        opening parenthesis, and extend our valid substring accordingly.

        Approach:
        1. Create a DP array where dp[i] represents the length of valid parentheses ending at position i
        2. For each closing parenthesis at position i:
           a. Check if it forms a direct pair with the previous character
           b. If not, check if it closes a valid substring followed by an opening parenthesis
        3. Return the maximum value in the DP array

        Complexity:
        Time: O(n) where n is the length of the string
        Space: O(n) for the DP array
        """
        if not s:
            return 0

        string_length = len(s)
        dp = [0] * (string_length + 1)

        for i, char in enumerate(s, 1):
            if char == ")":
                # Case 1: Direct pair "()"
                if i > 1 and s[i - 2] == "(":
                    dp[i] = dp[i - 2] + 2
                # Case 2: Nested pair "(...)"
                else:
                    prev_open_pos = i - dp[i - 1] - 1
                    if prev_open_pos >= 0 and s[prev_open_pos] == "(":
                        dp[i] = dp[i - 1] + 2
                        # Add length of any valid substring before this pair
                        if prev_open_pos > 0:
                            dp[i] += dp[prev_open_pos]

        return max(dp) if dp else 0
