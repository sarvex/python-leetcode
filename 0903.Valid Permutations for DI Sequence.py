class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """Dynamic programming with prefix sum accumulation.

        Intuition:
            For each position in the permutation, the valid choices depend on
            whether the current character is 'D' (decreasing) or 'I' (increasing).
            We can build the count of valid permutations using DP where f[i][j]
            represents permutations of length i+1 ending with the j-th smallest
            unused element.

        Approach:
            1. Initialize dp table f where f[0][0] = 1.
            2. For each character in the string, accumulate valid permutation
               counts based on whether it is 'D' or 'I'.
            3. For 'D', sum from j to i-1; for 'I', sum from 0 to j-1.
            4. Return the sum of all values in the last row.

        Complexity:
            Time: O(n^3)
            Space: O(n^2)
        """
        modulo = 10**9 + 7
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        dp[0][0] = 1
        for idx, char in enumerate(s, 1):
            if char == "D":
                for pos in range(idx + 1):
                    for prev in range(pos, idx):
                        dp[idx][pos] = (dp[idx][pos] + dp[idx - 1][prev]) % modulo
            else:
                for pos in range(idx + 1):
                    for prev in range(pos):
                        dp[idx][pos] = (dp[idx][pos] + dp[idx - 1][prev]) % modulo
        return sum(dp[length][pos] for pos in range(length + 1)) % modulo
