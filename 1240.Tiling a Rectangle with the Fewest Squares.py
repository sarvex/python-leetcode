class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        """Find the minimum number of squares to tile an n x m rectangle.

        Intuition:
            This is an NP-hard problem with no known polynomial solution.
            Backtracking with pruning explores all valid placements while
            cutting branches that cannot improve the current best.

        Approach:
            Scan cells left-to-right, top-to-bottom. At each unfilled cell,
            try placing the largest possible square that fits. Use a bitmask
            per row to track filled cells. Prune when the current count plus
            one already meets or exceeds the best answer found so far.

        Complexity:
            Time: O(exponential) - backtracking with pruning
            Space: O(n * m)
        """

        def search(row: int, col: int, count: int) -> None:
            nonlocal best
            if col == m:
                row += 1
                col = 0
            if row == n:
                best = count
                return
            if filled[row] >> col & 1:
                search(row, col + 1, count)
            elif count + 1 < best:
                max_rows = 0
                for k in range(row, n):
                    if filled[k] >> col & 1:
                        break
                    max_rows += 1
                max_cols = 0
                for k in range(col, m):
                    if filled[row] >> k & 1:
                        break
                    max_cols += 1
                max_side = min(max_rows, max_cols)
                for side in range(1, max_side + 1):
                    for k in range(side):
                        filled[row + side - 1] |= 1 << (col + k)
                        filled[row + k] |= 1 << (col + side - 1)
                    search(row, col + side, count + 1)
                for x in range(row, row + max_side):
                    for y in range(col, col + max_side):
                        filled[x] ^= 1 << y

        best = n * m
        filled = [0] * n
        search(0, 0, 0)
        return best
