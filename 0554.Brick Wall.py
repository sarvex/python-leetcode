from collections import defaultdict


class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        """Find the vertical line crossing the fewest bricks using edge counting.

        Intuition:
            A vertical line crosses fewer bricks where more brick edges align.
            Count edge positions across all rows and find the most common one.

        Approach:
            1. For each row, compute cumulative widths (excluding the last brick).
            2. Count how many rows have an edge at each position.
            3. The answer is total rows minus the maximum edge count.

        Complexity:
            Time: O(n) where n is the total number of bricks
            Space: O(w) where w is the wall width
        """
        edge_count: dict[int, int] = defaultdict(int)
        for row in wall:
            width = 0
            for brick in row[:-1]:
                width += brick
                edge_count[width] += 1
        if not edge_count:
            return len(wall)
        return len(wall) - edge_count[max(edge_count, key=edge_count.get)]
