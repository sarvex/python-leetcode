class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        """Valid Boomerang using cross product for collinearity check.

        Intuition:
            Three points form a boomerang if and only if they are not
            collinear, which can be tested using the cross product.

        Approach:
            Compute the cross product of vectors (p1->p2) and (p2->p3).
            If the cross product is non-zero, the points are non-collinear.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
