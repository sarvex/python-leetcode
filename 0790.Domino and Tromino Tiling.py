from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        """
        Dynamic Programming with State Representation

        Intuition:
        The problem can be modeled as filling a 2×n board with dominos and trominos.
        We can use DP with state representation where we track the progress of filling
        both rows of the board.

        Approach:
        1. Define a state (i, j) where i and j represent how far we've filled each row
        2. Use recursion with memoization to explore all possible ways to place tiles
        3. Handle three cases:
           - When both rows are at the same position (i == j)
           - When first row is ahead (i > j)
           - When second row is ahead (i < j)

        Complexity:
        Time: O(n) as we have at most O(n²) states and each state is computed once
        Space: O(n²) for the memoization cache
        """
        MOD = 10**9 + 7

        @cache
        def dp(i: int, j: int) -> int:
            # Base cases
            if i > n or j > n:
                return 0
            if i == n and j == n:
                return 1

            # Calculate possible ways based on current state
            if i == j:
                # Both rows aligned - can place horizontal/vertical dominos or trominos
                return (dp(i + 2, j + 2) +    # Horizontal dominos
                        dp(i + 1, j + 1) +    # Vertical dominos
                        dp(i + 2, j + 1) +    # Tromino type 1
                        dp(i + 1, j + 2)) % MOD  # Tromino type 2
            elif i > j:
                # First row ahead - place horizontal domino or tromino in second row
                return (dp(i, j + 2) + dp(i + 1, j + 2)) % MOD
            else:
                # Second row ahead - place horizontal domino or tromino in first row
                return (dp(i + 2, j) + dp(i + 2, j + 1)) % MOD

        return dp(0, 0)
