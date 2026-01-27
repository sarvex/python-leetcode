class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        """Check if a circle and axis-aligned rectangle overlap.

        Intuition:
            Find the closest point on the rectangle to the circle center,
            then check if the distance is within the radius.

        Approach:
            For each axis, compute the distance from the circle center to
            the nearest edge of the rectangle (clamped to zero if inside).
            Check if the squared distance is at most radius squared.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        def closest_distance(low: int, high: int, center: int) -> int:
            if low <= center <= high:
                return 0
            return low - center if center < low else center - high

        dx = closest_distance(x1, x2, xCenter)
        dy = closest_distance(y1, y2, yCenter)
        return dx * dx + dy * dy <= radius * radius
