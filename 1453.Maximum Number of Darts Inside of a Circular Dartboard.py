from math import sqrt, dist


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        """Find maximum darts inside a circle of radius r using circle centers.

        Intuition:
            The optimal circle must pass through at least two darts, so
            enumerate all pairs and check both possible circle centers.

        Approach:
            For each pair of darts, compute the two possible circle centers.
            For each candidate center, count how many darts fall within radius r.
            Track the global maximum.

        Complexity:
            Time: O(n^3) for pairs times counting
            Space: O(1)
        """

        def count_darts_in_circle(center_x: float, center_y: float) -> int:
            count = 0
            for dart_x, dart_y in darts:
                if dist((center_x, center_y), (dart_x, dart_y)) <= r + 1e-7:
                    count += 1
            return count

        def possible_centers(
            x1: float, y1: float, x2: float, y2: float
        ) -> list[tuple[float, float]]:
            dx, dy = x2 - x1, y2 - y1
            d = sqrt(dx * dx + dy * dy)
            if d > 2 * r:
                return []
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            dist_to_center = sqrt(r * r - (d / 2) * (d / 2))
            offset_x = dist_to_center * dy / d
            offset_y = dist_to_center * -dx / d
            return [
                (mid_x + offset_x, mid_y + offset_y),
                (mid_x - offset_x, mid_y - offset_y),
            ]

        num_darts = len(darts)
        max_darts = 1

        for i in range(num_darts):
            for j in range(i + 1, num_darts):
                centers = possible_centers(
                    darts[i][0], darts[i][1], darts[j][0], darts[j][1]
                )
                for center in centers:
                    max_darts = max(
                        max_darts, count_darts_in_circle(center[0], center[1])
                    )

        return max_darts
