from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Greedy approach using end-point sorting

        Intuition:
        Sort balloons by their end points and shoot arrows at the earliest possible
        position (the end point of the first balloon). This ensures we burst as many
        balloons as possible with each arrow.

        Approach:
        1. Sort all balloons by their end points
        2. Shoot an arrow at the end point of the first balloon
        3. Skip all balloons that can be burst by this arrow
        4. Repeat the process for the remaining balloons

        Complexity:
        Time: O(n log n) due to sorting
        Space: O(1) using only constant extra space
        """
        if not points:
            return 0

        # Sort balloons by their end points
        points.sort(key=lambda x: x[1])

        arrows = 1  # Start with one arrow
        position = points[0][1]  # Position of the first arrow

        # Check each balloon
        for start, end in points[1:]:
            # If current balloon starts after the last arrow position
            # we need a new arrow
            if start > position:
                arrows += 1
                position = end  # Update arrow position to the end of current balloon

        return arrows
