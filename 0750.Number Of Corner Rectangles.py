from collections import Counter


class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        """Count corner rectangles using column-pair frequency tracking.

        Intuition:
            A corner rectangle is formed by two rows sharing 1s in the same two
            columns. For each row, count how many previous rows share each
            column pair.

        Approach:
            1. For each row, find all pairs of columns with value 1.
            2. For each such pair, add the number of times this pair was seen
               in previous rows (each previous occurrence forms a rectangle).
            3. Increment the pair counter.

        Complexity:
            Time: O(R * C^2) where R = rows, C = columns
            Space: O(C^2)
        """
        result = 0
        pair_count: Counter[tuple[int, int]] = Counter()
        num_cols = len(grid[0])
        for row in grid:
            for i, val1 in enumerate(row):
                if val1:
                    for j in range(i + 1, num_cols):
                        if row[j]:
                            result += pair_count[(i, j)]
                            pair_count[(i, j)] += 1
        return result
