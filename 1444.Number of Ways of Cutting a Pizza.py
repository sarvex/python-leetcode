from functools import cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        """Count ways to cut pizza into k pieces each containing at least one apple.

        Intuition:
            Use 2D prefix sums to quickly check if a rectangular region has
            apples, then recursively try all horizontal and vertical cuts.

        Approach:
            Build a 2D prefix sum of apple counts. Use memoized recursion with
            state (top-left corner row, column, remaining cuts). At each state,
            try all horizontal cuts (varying row) and vertical cuts (varying
            column), only proceeding if the cut-off piece has at least one apple.

        Complexity:
            Time: O(k * m * n * (m + n)) for states times cut choices
            Space: O(k * m * n) for memoization
        """
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row_idx, row in enumerate(pizza, 1):
            for col_idx, char in enumerate(row, 1):
                prefix[row_idx][col_idx] = (
                    prefix[row_idx - 1][col_idx]
                    + prefix[row_idx][col_idx - 1]
                    - prefix[row_idx - 1][col_idx - 1]
                    + int(char == "A")
                )

        @cache
        def search(top: int, left: int, cuts_remaining: int) -> int:
            if cuts_remaining == 0:
                return int(
                    prefix[rows][cols]
                    - prefix[top][cols]
                    - prefix[rows][left]
                    + prefix[top][left]
                    > 0
                )
            total = 0
            for row_cut in range(top + 1, rows):
                if (
                    prefix[row_cut][cols]
                    - prefix[top][cols]
                    - prefix[row_cut][left]
                    + prefix[top][left]
                    > 0
                ):
                    total += search(row_cut, left, cuts_remaining - 1)
            for col_cut in range(left + 1, cols):
                if (
                    prefix[rows][col_cut]
                    - prefix[top][col_cut]
                    - prefix[rows][left]
                    + prefix[top][left]
                    > 0
                ):
                    total += search(top, col_cut, cuts_remaining - 1)
            return total % MOD

        return search(0, 0, k - 1)
