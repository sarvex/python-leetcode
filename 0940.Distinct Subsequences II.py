class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """DP tracking distinct subsequences ending at each character.

        Intuition:
            For each new character, the number of distinct subsequences ending with
            that character equals the total distinct subsequences so far plus one
            (the character alone). This avoids double-counting.

        Approach:
            1. Use a 2D DP where dp[i][c] = count of distinct subsequences of s[:i] ending with character c.
            2. For each character, set its count to sum of all previous counts + 1.
            3. Copy other character counts unchanged.
            4. Final answer is sum of all character counts modulo 10^9+7.

        Complexity:
            Time: O(n * 26) — iterate through string with 26 character slots
            Space: O(n * 26) — DP table
        """
        MOD = 10**9 + 7
        length = len(s)
        dp = [[0] * 26 for _ in range(length + 1)]
        for idx, char in enumerate(s, 1):
            char_index = ord(char) - ord("a")
            for letter in range(26):
                if letter == char_index:
                    dp[idx][letter] = sum(dp[idx - 1]) % MOD + 1
                else:
                    dp[idx][letter] = dp[idx - 1][letter]
        return sum(dp[-1]) % MOD
