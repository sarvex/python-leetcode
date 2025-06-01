from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two-pointer approach to find container with most water

        Intuition:
        The amount of water contained depends on the shorter height and the distance between lines.
        We can start with the widest container and move inward, always discarding the shorter line.

        Approach:
        1. Use two pointers starting from both ends of the array
        2. Calculate area as (right - left) * min(height[left], height[right])
        3. Move the pointer with the shorter height inward
        4. Keep track of the maximum area seen so far

        Complexity:
        Time: O(n) where n is the length of the height array (single pass)
        Space: O(1) as we only use constant extra space
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer with shorter height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
