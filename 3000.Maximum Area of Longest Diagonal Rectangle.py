from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """Find the area of the rectangle with the longest diagonal.

        Tagline: Compare squared diagonals to avoid square roots and track max area.

        Intuition:
            The rectangle with the longest diagonal maximizes sqrt(l^2 + w^2).
            Since sqrt is monotonic, comparing l^2 + w^2 suffices. On ties, pick
            the larger area.

        Approach:
            Iterate all pairs (l, w). Maintain the best squared diagonal seen so far
            and the corresponding maximum area. Update when a strictly larger
            squared diagonal is found; on equal squared diagonal, maximize by area.

        Complexity:
            Time: O(n), where n is the number of rectangles.
            Space: O(1).
        """

        max_diag_sq: int = 0
        max_area: int = 0

        for length, width in dimensions:
            diag_sq = length * length + width * width
            area = length * width

            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = area
            elif diag_sq == max_diag_sq and area > max_area:
                max_area = area

        return max_area
