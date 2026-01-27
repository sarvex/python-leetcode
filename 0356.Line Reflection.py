from math import inf


class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        """Check if all points reflect across a vertical line.

        Intuition:
            The reflection line must be at x = (min_x + max_x) / 2. For every
            point (x, y), the reflected point (sum - x, y) must also exist.

        Approach:
            1. Find min and max x-coordinates to determine the reflection axis.
            2. Store all points in a set for O(1) lookup.
            3. Verify that every point has its reflection in the set.

        Complexity:
            Time: O(n) where n is the number of points
            Space: O(n) for the point set
        """
        min_x, max_x = inf, -inf
        point_set: set[tuple[int, int]] = set()
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))
        axis_sum = min_x + max_x
        return all((axis_sum - x, y) in point_set for x, y in points)
