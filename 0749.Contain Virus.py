class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        """Simulation with BFS/DFS to quarantine the most threatening virus region.

        Intuition:
            Each day, identify all infected regions, quarantine the one threatening
            the most uninfected cells, then let remaining regions spread.

        Approach:
            1. DFS to find connected infected regions, tracking their boundaries
               and wall counts.
            2. Quarantine the region with the largest boundary (mark cells -1).
            3. Spread infection from all other regions.
            4. Repeat until no more regions exist.

        Complexity:
            Time: O(M * N * max_rounds)
            Space: O(M * N)
        """

        def search(row: int, col: int) -> None:
            visited[row][col] = True
            areas[-1].append((row, col))
            for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                    if (
                        isInfected[next_row][next_col] == 1
                        and not visited[next_row][next_col]
                    ):
                        search(next_row, next_col)
                    elif isInfected[next_row][next_col] == 0:
                        wall_counts[-1] += 1
                        boundaries[-1].add((next_row, next_col))

        num_rows, num_cols = len(isInfected), len(isInfected[0])
        total_walls = 0
        while True:
            visited = [[False] * num_cols for _ in range(num_rows)]
            areas: list[list[tuple[int, int]]] = []
            wall_counts: list[int] = []
            boundaries: list[set[tuple[int, int]]] = []
            for i, row in enumerate(isInfected):
                for j, val in enumerate(row):
                    if val == 1 and not visited[i][j]:
                        areas.append([])
                        boundaries.append(set())
                        wall_counts.append(0)
                        search(i, j)
            if not areas:
                break
            quarantine_idx = boundaries.index(max(boundaries, key=len))
            total_walls += wall_counts[quarantine_idx]
            for region_idx, area in enumerate(areas):
                if region_idx == quarantine_idx:
                    for row, col in area:
                        isInfected[row][col] = -1
                else:
                    for row, col in area:
                        for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            next_row, next_col = row + delta_row, col + delta_col
                            if (
                                0 <= next_row < num_rows
                                and 0 <= next_col < num_cols
                                and isInfected[next_row][next_col] == 0
                            ):
                                isInfected[next_row][next_col] = 1
        return total_walls
