class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: list[int]
    ) -> list[list[int]]:
        """Reconstruct a 2-row binary matrix from column sums greedily.

        Intuition:
            Columns with sum 2 must have both rows set to 1. Columns with sum 1
            should assign the 1 to whichever row has more remaining capacity to
            maintain balance.

        Approach:
            First assign both 1s for columns with sum 2, decrementing both row
            budgets. Then for columns with sum 1, assign to the row with higher
            remaining budget. If at any point a budget goes negative or budgets
            are not zero at the end, return empty.

        Complexity:
            Time: O(n) — single pass through column sums
            Space: O(n) — for the result matrix
        """
        num_cols = len(colsum)
        result = [[0] * num_cols for _ in range(2)]
        for j, total in enumerate(colsum):
            if total == 2:
                result[0][j] = result[1][j] = 1
                upper -= 1
                lower -= 1
            if total == 1:
                if upper > lower:
                    upper -= 1
                    result[0][j] = 1
                else:
                    lower -= 1
                    result[1][j] = 1
            if upper < 0 or lower < 0:
                return []
        return result if lower == upper == 0 else []
