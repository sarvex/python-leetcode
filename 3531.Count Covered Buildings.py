from typing import List
import collections


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        """
        Counts the number of covered buildings.
        A building at (r, c) is covered if there is at least one building
        in each of the 4 directions: above (r' < r, c' = c), below (r' > r, c' = c),
        left (r' = r, c' < c), and right (r' = r, c' > c).
        """
        # We need to find the min_row, max_row for each column
        # and min_col, max_col for each row.

        row_min_col = collections.defaultdict(lambda: float("inf"))
        row_max_col = collections.defaultdict(lambda: float("-inf"))
        col_min_row = collections.defaultdict(lambda: float("inf"))
        col_max_row = collections.defaultdict(lambda: float("-inf"))

        for r, c in buildings:
            row_min_col[r] = min(row_min_col[r], c)
            row_max_col[r] = max(row_max_col[r], c)
            col_min_row[c] = min(col_min_row[c], r)
            col_max_row[c] = max(col_max_row[c], r)

        count = 0
        for r, c in buildings:
            # Check if covered
            # Left: exists (r, c_left) with c_left < c => min_col[r] < c
            # Right: exists (r, c_right) with c_right > c => max_col[r] > c
            # Above: exists (r_above, c) with r_above < r => min_row[c] < r
            # Below: exists (r_below, c) with r_below > r => max_row[c] > r

            if (
                row_min_col[r] < c
                and row_max_col[r] > c
                and col_min_row[c] < r
                and col_max_row[c] > r
            ):
                count += 1

        return count
