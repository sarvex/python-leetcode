class Solution:
    def isConvex(self, points: list[list[int]]) -> bool:
        """Cross product sign consistency check for convexity.

        Intuition:
            A polygon is convex if all cross products of consecutive edge
            vectors have the same sign, meaning all turns go in the same
            direction.

        Approach:
            For each triplet of consecutive vertices, compute the cross
            product of the two edge vectors. If any non-zero cross product
            has a different sign than the previous non-zero one, the polygon
            is not convex.

        Complexity:
            Time: O(n) where n is the number of points
            Space: O(1)
        """
        num_points = len(points)
        previous_cross = current_cross = 0
        for i in range(num_points):
            dx1 = points[(i + 1) % num_points][0] - points[i][0]
            dy1 = points[(i + 1) % num_points][1] - points[i][1]
            dx2 = points[(i + 2) % num_points][0] - points[i][0]
            dy2 = points[(i + 2) % num_points][1] - points[i][1]
            current_cross = dx1 * dy2 - dx2 * dy1
            if current_cross != 0:
                if current_cross * previous_cross < 0:
                    return False
                previous_cross = current_cross
        return True
