class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """Dynamic programming to find minimum window subsequence.

        Intuition:
            Track the starting position of a valid subsequence match ending at
            each position. Use DP where dp[i][j] stores the start index in s1
            where matching s2[:j] begins when considering s1[:i].

        Approach:
            1. Build dp[i][j] = starting index in s1 of the best match for
               s2[:j] using s1[:i].
            2. If s1[i-1] == s2[j-1] and j == 1, the start is i itself.
            3. If characters match, inherit from dp[i-1][j-1]; otherwise from
               dp[i-1][j].
            4. Scan the last column to find the shortest window.

        Complexity:
            Time: O(m * n) where m, n are lengths of s1, s2
            Space: O(m * n) for the DP table
        """
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i, char1 in enumerate(s1, 1):
            for j, char2 in enumerate(s2, 1):
                if char1 == char2:
                    dp[i][j] = i if j == 1 else dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        start, min_length = 0, len1 + 1
        for i, char1 in enumerate(s1, 1):
            if char1 == s2[len2 - 1] and dp[i][len2]:
                window_start = dp[i][len2] - 1
                if i - window_start < min_length:
                    min_length = i - window_start
                    start = window_start
        return "" if min_length > len1 else s1[start : start + min_length]
