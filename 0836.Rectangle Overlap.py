class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        """Check rectangle overlap by negating non-overlap conditions.

        Intuition:
            Two rectangles do NOT overlap if one is completely to the left,
            right, above, or below the other. Negate these conditions.

        Approach:
            1. Unpack both rectangle coordinates.
            2. Return True if none of the four non-overlap conditions hold.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)
