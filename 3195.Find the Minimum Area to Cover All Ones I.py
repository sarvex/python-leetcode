from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Approach: Track row bounds and column bounds in a single pass using index scans

        Intuition: The minimal covering rectangle is bounded by the first/last rows
        containing 1 and the leftmost/rightmost columns containing 1 across those rows.

        Approach: For each row that contains a 1, update top/bottom row indices.
        Use row.index(1) for leftmost and len(row) - 1 - row[::-1].index(1) for rightmost.
        Finally compute area = (bottom - top + 1) * (right - left + 1).

        Complexity:
        Time: O(m*n)
        Space: O(1)
        """
        top = -1
        bottom = -1
        left = float("inf")
        right = -1

        for i, row in enumerate(grid):
            if 1 in row:
                if top == -1:
                    top = i
                bottom = i
                li = row.index(1)
                ri = len(row) - 1 - row[::-1].index(1)
                if li < left:
                    left = li
                if ri > right:
                    right = ri

        if top == -1:
            return 0

        height = bottom - top + 1
        width = right - left + 1
        return height * width
