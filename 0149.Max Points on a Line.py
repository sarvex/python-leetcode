class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """Brute Force Collinearity Check.

        Intuition:
            Three points are collinear if the cross product of vectors formed
            by them equals zero. Check all triplets using this property.

        Approach:
            For each pair of points, count how many other points are collinear
            with them by checking if the cross product of direction vectors
            is zero. Track the maximum count.

        Complexity:
            Time: O(n^3) for checking all triplets
            Space: O(1) no extra data structures used
        """
        num_points = len(points)
        result = 1
        for i in range(num_points):
            x1, y1 = points[i]
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                count = 2
                for k in range(j + 1, num_points):
                    x3, y3 = points[k]
                    cross_a = (y2 - y1) * (x3 - x1)
                    cross_b = (y3 - y1) * (x2 - x1)
                    count += cross_a == cross_b
                result = max(result, count)
        return result
