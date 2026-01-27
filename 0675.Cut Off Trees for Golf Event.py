from heapq import heappop, heappush


class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        """A* search to cut trees in height order.

        Intuition:
            Trees must be cut in order of height. For each consecutive pair of
            trees we need the shortest path, which can be found with A* using
            Manhattan distance as the heuristic.

        Approach:
            1. Collect all trees with height > 1 and sort by height.
            2. For each consecutive pair of trees, run A* search to find the
               shortest walking distance on the grid.
            3. Accumulate total steps; return -1 if any tree is unreachable.

        Complexity:
            Time: O(m^2 * n^2) worst case for each A* search across all trees
            Space: O(m * n) for the distance map in each search
        """

        def manhattan(row1: int, col1: int, row2: int, col2: int) -> int:
            return abs(row1 - row2) + abs(col1 - col2)

        def search(
            start_row: int, start_col: int, target_row: int, target_col: int
        ) -> int:
            heap = [
                (
                    manhattan(start_row, start_col, target_row, target_col),
                    start_row,
                    start_col,
                )
            ]
            dist = {start_row * cols + start_col: 0}
            while heap:
                _, row, col = heappop(heap)
                step = dist[row * cols + col]
                if (row, col) == (target_row, target_col):
                    return step
                for delta_row, delta_col in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    next_row, next_col = row + delta_row, col + delta_col
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and forest[next_row][next_col] > 0
                    ):
                        key = next_row * cols + next_col
                        if key not in dist or dist[key] > step + 1:
                            dist[key] = step + 1
                            heappush(
                                heap,
                                (
                                    dist[key]
                                    + manhattan(
                                        next_row, next_col, target_row, target_col
                                    ),
                                    next_row,
                                    next_col,
                                ),
                            )
            return -1

        rows, cols = len(forest), len(forest[0])
        trees = [
            (forest[i][j], i, j)
            for i in range(rows)
            for j in range(cols)
            if forest[i][j] > 1
        ]
        trees.sort()
        current_row = current_col = 0
        total_steps = 0
        for _, target_row, target_col in trees:
            steps = search(current_row, current_col, target_row, target_col)
            if steps == -1:
                return -1
            total_steps += steps
            current_row, current_col = target_row, target_col
        return total_steps
