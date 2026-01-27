class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        """Inclusion-exclusion to compute total area of two rectangles.

        Intuition:
            The total area equals the sum of both rectangles minus their
            overlapping region (if any).

        Approach:
            1. Compute area of each rectangle independently.
            2. Calculate overlap width and height (clamped to zero if no overlap).
            3. Subtract the overlap area from the sum.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        return area_a + area_b - max(overlap_height, 0) * max(overlap_width, 0)
