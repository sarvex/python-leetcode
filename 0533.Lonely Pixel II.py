from collections import defaultdict


class Solution:
    def findBlackPixel(self, picture: list[list[str]], target: int) -> int:
        """Count black pixels in rows with exactly target black pixels and identical rows.

        Intuition:
            A black pixel qualifies if its row has exactly target black pixels
            and all rows containing a black pixel in that column are identical.

        Approach:
            Count black pixels per row and group row indices by column.
            For each column, check if the first row has target black pixels,
            all grouped rows are identical, and the count matches target.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        row_counts = [0] * len(picture)
        col_to_rows: dict[int, list[int]] = defaultdict(list)
        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == "B":
                    row_counts[i] += 1
                    col_to_rows[j].append(i)
        result = 0
        for col_idx in col_to_rows:
            first_row = col_to_rows[col_idx][0]
            if row_counts[first_row] != target:
                continue
            if len(col_to_rows[col_idx]) == row_counts[first_row] and all(
                picture[other_row] == picture[first_row]
                for other_row in col_to_rows[col_idx]
            ):
                result += target
        return result
