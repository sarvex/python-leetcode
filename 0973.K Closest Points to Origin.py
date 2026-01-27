from math import hypot


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """Sort points by Euclidean distance and return the k closest.

        Intuition:
        The k closest points to the origin have the smallest Euclidean
        distances. Sorting by distance and slicing gives the answer directly.

        Approach:
        1. Sort all points by their distance from origin using hypot
        2. Return the first k points from the sorted list

        Complexity:
        Time: O(n log n) for sorting
        Space: O(n) for the sorted result
        """
        points.sort(key=lambda p: hypot(p[0], p[1]))
        return points[:k]
