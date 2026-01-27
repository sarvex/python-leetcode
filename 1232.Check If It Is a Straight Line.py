class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        """Check if all points lie on a single straight line.

        Intuition:
            Three points are collinear if the cross product of the vectors
            formed by the first point to the other two is zero.

        Approach:
            Fix the first two points to define the line. For every subsequent
            point, verify collinearity using the cross product formula to
            avoid division and floating point issues.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates[2:]:
            if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
                return False
        return True
