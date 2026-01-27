class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """Dynamic Programming Approach

        Intuition:
            We can check if a string can be segmented by checking if any prefix
            is a valid word and the remainder can also be segmented. This has
            optimal substructure suitable for DP.

        Approach:
            Use a boolean DP array where dp[i] indicates if s[0..i-1] can be
            segmented. For each position i, check all possible split points j
            where dp[j] is true and s[j:i] is in the word dictionary.

        Complexity:
            Time: O(n^2 * m) where n is string length, m is average word length for hashing
            Space: O(n + k) where k is total characters in wordDict
        """
        words = set(wordDict)
        length = len(s)
        dp = [True] + [False] * length
        for i in range(1, length + 1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[length]
