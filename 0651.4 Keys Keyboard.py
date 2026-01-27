class Solution:
    def maxA(self, n: int) -> int:
        """DP finding optimal point to start copy-paste sequence for max A's.

        Intuition:
        At some point, it becomes more efficient to select-all, copy, then paste
        multiple times rather than pressing A individually. Try all breakpoints.

        Approach:
        1. Initialize dp[i] = i (just pressing A i times).
        2. For each position i >= 3, try all breakpoints j where we select-all, copy
           at position j-1, then paste (i-j) times, giving dp[j-1] * (i-j) A's.
        3. Return dp[n].

        Complexity:
        Time: O(n^2)
        Space: O(n)
        """
        dp = list(range(n + 1))
        for i in range(3, n + 1):
            for j in range(2, i - 1):
                dp[i] = max(dp[i], dp[j - 1] * (i - j))
        return dp[-1]
