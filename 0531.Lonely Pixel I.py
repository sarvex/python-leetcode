class Solution:
    def findLonelyPixel(self, picture: list[list[str]]) -> int:
        """Count black pixels that are alone in their row and column.

        Intuition:
            A pixel is lonely if it is the only black pixel in its row and
            column. Count black pixels per row and column first.

        Approach:
            First pass: count black pixels in each row and column.
            Second pass: count black pixels where both row and column counts are 1.

        Complexity:
            Time: O(m * n)
            Space: O(m + n)
        """
        row_counts = [0] * len(picture)
        col_counts = [0] * len(picture[0])
        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == "B":
                    row_counts[i] += 1
                    col_counts[j] += 1
        result = 0
        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == "B" and row_counts[i] == 1 and col_counts[j] == 1:
                    result += 1
        return result
