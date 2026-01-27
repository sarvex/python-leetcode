from itertools import pairwise


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        """Backtracking DFS counting paths that visit every non-obstacle cell exactly once.

        Intuition:
        We need to find all paths from start to end that cover every walkable
        cell. Backtracking with a visited set naturally explores and counts
        all valid Hamiltonian paths.

        Approach:
        1. Find start position and count walkable cells (value 0)
        2. DFS from start, marking cells as visited
        3. At the end cell, check if all walkable cells were visited
        4. Backtrack by removing cells from visited set

        Complexity:
        Time: O(3^(m*n)) worst case for branching at each cell
        Space: O(m * n) for the visited set and recursion stack
        """
        rows, cols = len(grid), len(grid[0])
        start = next(
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if grid[row][col] == 1
        )
        directions = (-1, 0, 1, 0, -1)
        walkable_count = sum(row.count(0) for row in grid)
        visited: set[tuple[int, int]] = {start}

        def search(row: int, col: int, steps: int) -> int:
            if grid[row][col] == 2:
                return int(steps == walkable_count + 1)
            path_count = 0
            for delta_row, delta_col in pairwise(directions):
                new_row, new_col = row + delta_row, col + delta_col
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and (new_row, new_col) not in visited
                    and grid[new_row][new_col] != -1
                ):
                    visited.add((new_row, new_col))
                    path_count += search(new_row, new_col, steps + 1)
                    visited.remove((new_row, new_col))
            return path_count

        return search(*start, 0)
