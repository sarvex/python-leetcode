from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Space-optimized Dynamic Programming approach for minimum path sum.

        Intuition:
            We can optimize the space complexity by using just a 1D array,
            since we only need the previous row's values to compute the current row.

        Approach:
            1. Create a 1D DP array of length equal to the number of columns
            2. Process the grid row by row, updating the DP array in-place
            3. Return the last element of the DP array after processing all rows

        Complexity:
            Time: O(m*n) where m and n are the dimensions of the grid
            Space: O(n) where n is the number of columns
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        # Initialize first row
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        # Process remaining rows
        for i in range(1, m):
            dp[0] += grid[i][0]  # Update first element of current row
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[n-1]
