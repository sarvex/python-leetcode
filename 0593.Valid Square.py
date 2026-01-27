class Solution:
    def validSquare(
        self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]
    ) -> bool:
        """Check if four points form a valid square by verifying distance properties.

        Intuition:
            For any three points of a square, two distances must be equal (sides)
            and their sum must equal the third distance (diagonal), using the
            Pythagorean theorem.

        Approach:
            1. Define a helper that checks if three points form a right isosceles
               triangle (a corner of a square).
            2. Verify this property holds for all four combinations of three points.
            3. All checks passing confirms a valid square.

        Complexity:
            Time: O(1)
            Space: O(1)
        """

        def check(point_a: list[int], point_b: list[int], point_c: list[int]) -> bool:
            (x1, y1), (x2, y2), (x3, y3) = point_a, point_b, point_c
            dist1 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            dist2 = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)
            dist3 = (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)
            return any(
                [
                    dist1 == dist2 and dist1 + dist2 == dist3 and dist1,
                    dist2 == dist3 and dist2 + dist3 == dist1 and dist2,
                    dist1 == dist3 and dist1 + dist3 == dist2 and dist1,
                ]
            )

        return (
            check(p1, p2, p3)
            and check(p2, p3, p4)
            and check(p1, p3, p4)
            and check(p1, p2, p4)
        )
