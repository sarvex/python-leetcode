class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Tagline: Two-pass diagonal sort (first-column desc, first-row asc) for TL-BR diagonals.

        Intuition: Each top-left to bottom-right diagonal can be handled independently by collecting
        its values, sorting them, and writing them back along the same path. Splitting by starting
        edges avoids overlap while covering all diagonals.

        Approach:
        - Pass 1: For starts (k, 0) for k in [0..n-1], collect diagonal, sort in descending order,
          then write back along the same diagonal.
        - Pass 2: For starts (0, k) for k in [1..n-1], collect diagonal, sort in ascending order,
          then write back along the same diagonal.

        Complexity:
        - Time: O(n^2 log n) overall (sum of diagonal sizes is n^2).
        - Space: O(n) for the largest diagonal buffer.
        """
        n = len(grid)

        def sort_diag(si: int, sj: int, reverse: bool) -> None:
            """Collect TL-BR diagonal from (si, sj), sort by `reverse`, and write back in order."""
            i, j = si, sj
            buf: list[int] = []
            while i < n and j < n:
                buf.append(grid[i][j])
                i += 1
                j += 1
            buf.sort(reverse=reverse)
            i, j = si, sj
            p = 0
            while i < n and j < n:
                grid[i][j] = buf[p]
                p += 1
                i += 1
                j += 1

        # Pass 1: diagonals starting from first column (descending)
        for k in range(n):
            sort_diag(k, 0, True)

        # Pass 2: diagonals starting from first row, excluding (0,0) (ascending)
        for k in range(1, n):
            sort_diag(0, k, False)

        return grid
