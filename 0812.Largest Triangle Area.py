class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """Brute-force all point triples using cross product area formula.

        Intuition:
            With at most 50 points, we can check all triples and compute the
            triangle area using the cross product formula.

        Approach:
            1. Iterate over all triples of points.
            2. Compute the area using |u1*v2 - u2*v1| / 2.
            3. Track the maximum area.

        Complexity:
            Time: O(n^3)
            Space: O(1)
        """
        max_area = 0
        for x1, y1 in points:
            for x2, y2 in points:
                for x3, y3 in points:
                    edge1_x, edge1_y = x2 - x1, y2 - y1
                    edge2_x, edge2_y = x3 - x1, y3 - y1
                    area = abs(edge1_x * edge2_y - edge2_x * edge1_y) / 2
                    max_area = max(max_area, area)
        return max_area
