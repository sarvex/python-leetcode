from itertools import product
from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Dynamic Programming approach to find unique paths from top-left to bottom-right.

        Intuition:
        At each cell, the number of ways to reach it is the sum of ways to reach the cell above
        and the cell to the left. This forms a classic dynamic programming problem.

        Approach:
        1. Create a 2D DP table where dp[i][j] represents unique paths to position (i,j)
        2. Initialize dp[0][0] = 1 (one way to reach the starting position)
        3. For each cell, calculate dp[i][j] = dp[i-1][j] + dp[i][j-1]
        4. Return dp[m-1][n-1] as the final answer

        Complexity:
        Time: O(m*n) - we visit each cell once
        Space: O(m*n) - for the dp table
        """
        # Initialize dp table with zeros
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Base case: one way to reach starting position

        # Fill dp table using itertools.product for cleaner iteration
        for i, j in product(range(m), range(n)):
            # Skip the starting position as it's already initialized
            if i == 0 and j == 0:
                continue
            # Add paths from above (if not in first row)
            if i > 0:
                dp[i][j] += dp[i-1][j]
            # Add paths from left (if not in first column)
            if j > 0:
                dp[i][j] += dp[i][j-1]

        return dp[m-1][n-1]

    def uniquePaths_math(self, m: int, n: int) -> int:
        """Mathematical combination approach to find unique paths.

        Intuition:
        To reach the bottom-right corner from top-left, we need to move exactly
        m-1 steps down and n-1 steps right, in any order. This is equivalent to
        choosing which of the total m+n-2 positions will be down-moves.

        Approach:
        Use the combination formula C(m+n-2, m-1) or C(m+n-2, n-1)

        Complexity:
        Time: O(min(m,n)) - for the combination calculation
        Space: O(1) - constant extra space
        """
        # Total steps needed: (m-1) down + (n-1) right = m+n-2 total steps
        # We need to choose which (m-1) positions out of (m+n-2) will be down-moves
        return comb(m + n - 2, m - 1)

    def uniquePaths_optimized(self, m: int, n: int) -> int:
        """Space-optimized DP approach to find unique paths.

        Intuition:
        We can optimize the space complexity by using a 1D array instead of a 2D array,
        as we only need the previous row's results to calculate the current row.

        Approach:
        1. Create a 1D DP array of size n
        2. For each row, update the array in-place
        3. Return dp[n-1] as the final answer

        Complexity:
        Time: O(m*n) - we visit each cell once
        Space: O(n) - for the 1D dp array
        """
        # Initialize dp array with 1s (each cell in first row has exactly 1 way)
        dp = [1] * n

        # Process each row (starting from second row)
        for _ in range(1, m):
            # Update dp array in-place (from left to right)
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[n-1]
