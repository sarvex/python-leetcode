class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Calculate the minimum path sum from top to bottom of the triangle using bottom-up DP with O(n) space.
        
        Intuition:
        - Traverse from bottom to top, keeping track of the minimum path sum for each position using a 1D array.
        
        Approach:
        - Initialize a DP array with size (n+1) where n is the number of rows in the triangle.
        - For each row from bottom to top, update the DP array by taking the minimum of adjacent elements.
        - The result will be stored in dp[0] after processing all rows.
        
        Complexity:
        - Time: O(n²) where n is the number of rows in the triangle
        - Space: O(n) where n is the number of rows in the triangle
        """
        dp = [0] * (len(triangle) + 1)
        for row in reversed(triangle):
            for i, num in enumerate(row):
                dp[i] = min(dp[i], dp[i + 1]) + num
        return dp[0]
