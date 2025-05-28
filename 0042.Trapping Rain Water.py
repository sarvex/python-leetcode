from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer approach to calculate trapped rainwater
        
        Intuition:
        Water can only be trapped if there are higher bars on both sides. The amount of
        water trapped at any position is determined by the minimum of the maximum heights
        to its left and right, minus the height at that position.
        
        Approach:
        1. Calculate the maximum height to the left of each position
        2. Calculate the maximum height to the right of each position
        3. For each position, calculate trapped water as min(left_max, right_max) - height
        4. Sum up all trapped water amounts
        
        Complexity:
        Time: O(n) where n is the length of the height array (two passes through the array)
        Space: O(n) for storing the left and right maximum height arrays
        """
        n = len(height)
        if n <= 2:
            return 0
            
        # Precompute maximum heights to the left and right
        left_max = [0] * n
        right_max = [0] * n
        
        # Initialize with first and last heights
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        
        # Fill left_max and right_max arrays
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            right_max[n-i-1] = max(right_max[n-i], height[n-i-1])
        
        # Calculate trapped water at each position and sum
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
