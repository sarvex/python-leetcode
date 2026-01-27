from collections import Counter


class Solution:
    def gridIllumination(
        self, n: int, lamps: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        """Answer illumination queries on a grid with lamps.

        Intuition:
            A cell is illuminated if any lamp shares its row, column, or diagonal.
            Use counters for rows, columns, and both diagonals to check in O(1).

        Approach:
            Store active lamps in a set and maintain counters for row, column,
            and both diagonal directions. For each query, check illumination then
            turn off all lamps in the 3×3 neighborhood, updating counters.

        Complexity:
            Time: O(L + Q) where L is lamps count and Q is queries count
            Space: O(L) for the lamp set and counters
        """
        active_lamps = {(r, c) for r, c in lamps}
        row_count: Counter[int] = Counter()
        col_count: Counter[int] = Counter()
        diag_count: Counter[int] = Counter()
        anti_diag_count: Counter[int] = Counter()
        for r, c in active_lamps:
            row_count[r] += 1
            col_count[c] += 1
            diag_count[r - c] += 1
            anti_diag_count[r + c] += 1
        result = [0] * len(queries)
        for idx, (qr, qc) in enumerate(queries):
            if (
                row_count[qr]
                or col_count[qc]
                or diag_count[qr - qc]
                or anti_diag_count[qr + qc]
            ):
                result[idx] = 1
            for dr in range(qr - 1, qr + 2):
                for dc in range(qc - 1, qc + 2):
                    if (dr, dc) in active_lamps:
                        active_lamps.remove((dr, dc))
                        row_count[dr] -= 1
                        col_count[dc] -= 1
                        diag_count[dr - dc] -= 1
                        anti_diag_count[dr + dc] -= 1
        return result
