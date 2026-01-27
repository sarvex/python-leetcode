from math import sqrt, atan2, acos


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        """Find maximum darts inside a circle of radius r using angular sweep.

        Intuition:
            For each dart as a reference point, use angular sweep to find
            the maximum number of other darts within a circle of radius r
            passing through the reference point.

        Approach:
            For each dart, compute entry and exit angles for all other darts
            within diameter distance. Sort angles and sweep to find the
            maximum overlap count, which gives the maximum darts in a circle.

        Complexity:
            Time: O(n^2 * log(n)) for angular sweep per point
            Space: O(n) for the angles list
        """
        result = 1
        for x, y in darts:
            angles: list[tuple[float, int]] = []
            for x1, y1 in darts:
                if (x1 != x or y1 != y) and (
                    distance := sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                ) <= 2 * r:
                    angle = atan2(y1 - y, x1 - x)
                    delta = acos(distance / (2 * r))
                    angles.append((angle - delta, +1))
                    angles.append((angle + delta, -1))
            angles.sort(key=lambda item: (item[0], -item[1]))
            current_count = 1
            for _, entry_flag in angles:
                current_count += entry_flag
                result = max(result, current_count)
        return result
