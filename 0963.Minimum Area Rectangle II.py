import math


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        """Brute-force check all point triples for axis-aligned-free rectangles.

        Intuition:
            For any three points forming a right angle, the fourth vertex is
            determined. Check if it exists and compute the area.

        Approach:
            1. Store all points in a set for O(1) lookup.
            2. For each triple (p1, p2, p3), compute the fourth point assuming
               p1 is the right-angle vertex.
            3. Verify the dot product of vectors p1->p2 and p1->p3 is zero.
            4. If the fourth point exists and angle is 90 degrees, compute area.
            5. Track the minimum area.

        Complexity:
            Time: O(n^3) — checking all point triples
            Space: O(n) — point set for lookup
        """
        point_set = {(x, y) for x, y in points}
        num_points = len(points)
        min_area = math.inf
        for i in range(num_points):
            x1, y1 = points[i]
            for j in range(num_points):
                if j != i:
                    x2, y2 = points[j]
                    for k in range(j + 1, num_points):
                        if k != i:
                            x3, y3 = points[k]
                            x4 = x2 - x1 + x3
                            y4 = y2 - y1 + y3
                            if (x4, y4) in point_set:
                                vec_a = (x2 - x1, y2 - y1)
                                vec_b = (x3 - x1, y3 - y1)
                                if vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1] == 0:
                                    width = math.sqrt(vec_a[0] ** 2 + vec_a[1] ** 2)
                                    height = math.sqrt(vec_b[0] ** 2 + vec_b[1] ** 2)
                                    min_area = min(min_area, width * height)
        return 0 if min_area == math.inf else min_area
