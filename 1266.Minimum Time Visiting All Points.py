from itertools import pairwise


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        """Find minimum time to visit all points in order on a 2D plane.

        Intuition:
            Moving diagonally covers both x and y distance simultaneously.
            The minimum time between two points is the Chebyshev distance.

        Approach:
            For each consecutive pair of points, compute the Chebyshev
            distance (max of absolute differences in x and y). Sum all
            such distances.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        return sum(
            max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) for p1, p2 in pairwise(points)
        )
