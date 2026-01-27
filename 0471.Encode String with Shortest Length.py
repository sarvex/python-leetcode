class Solution:
    def encode(self, s: str) -> str:
        """Interval DP with repeated substring pattern detection.

        Intuition:
            For each substring, check if it can be represented as a repeated
            pattern (e.g., 'abcabc' -> '2[abc]'). Combine this with optimal
            encodings of sub-intervals.

        Approach:
            Use a 2D DP table where dp[i][j] stores the shortest encoding
            of s[i..j]. For each interval, first check for a repeating
            pattern using the (t+t).index(t,1) trick. Then try all split
            points to find a shorter concatenation of sub-encodings.

        Complexity:
            Time: O(n^3) where n is the length of the string
            Space: O(n^2)
        """

        def find_encoding(left: int, right: int) -> str:
            substring = s[left : right + 1]
            if len(substring) < 5:
                return substring
            repeat_index = (substring + substring).index(substring, 1)
            if repeat_index < len(substring):
                repeat_count = len(substring) // repeat_index
                return f"{repeat_count}[{dp[left][left + repeat_index - 1]}]"
            return substring

        length = len(s)
        dp: list[list[str | None]] = [[None] * length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                dp[i][j] = find_encoding(i, j)
                if j - i + 1 > 4:
                    for k in range(i, j):
                        concatenated = dp[i][k] + dp[k + 1][j]
                        if len(dp[i][j]) > len(concatenated):
                            dp[i][j] = concatenated
        return dp[0][-1]
