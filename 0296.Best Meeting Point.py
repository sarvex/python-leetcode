class Solution:
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        """Median-based optimal meeting point on a 2D grid.

        Intuition:
            The optimal 1D meeting point minimizing total Manhattan distance is
            the median. This extends to 2D by independently finding the median
            row and median column of all people.

        Approach:
            1. Collect all row and column indices of people (grid value 1).
            2. Rows are naturally sorted by iteration order; sort columns separately.
            3. Find the median row and median column.
            4. Sum Manhattan distances from each person to the median point.

        Complexity:
            Time: O(m * n + k log k) where k is the number of people
            Space: O(k)
        """

        def total_distance(positions: list[int], center: int) -> int:
            return sum(abs(pos - center) for pos in positions)

        rows: list[int] = []
        cols: list[int] = []
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        median_row = rows[len(rows) >> 1]
        median_col = cols[len(cols) >> 1]
        return total_distance(rows, median_row) + total_distance(cols, median_col)
