class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """DP bottom-up counting of all-ones squares.

        Intuition:
            Each cell contributes the size of the largest all-ones square ending at it.
            If a cell is 1, its contribution is 1 plus the minimum of its top, left,
            and top-left DP neighbors; otherwise 0.

        Approach:
            - Use a 1D DP array where `dp[j]` stores the largest square size ending at
              current row and column `j`.
            - Track `prev` as the top-left neighbor (old `dp[j-1]` from previous row).
            - Transition (for 1 cells): `dp[j] = 1 + min(dp[j] /*top*/, dp[j-1] /*left*/, prev /*top-left*/)`.
            - Reset `dp[j]` to 0 for 0 cells and accumulate the running sum.

        Complexity:
            Time: O(m*n)
            Space: O(min(m, n))
        """

        rows: int = len(matrix)
        cols: int = len(matrix[0]) if rows else 0
        if rows == 0 or cols == 0:
            return 0

        # Ensure dp size is the smaller dimension for potential cache friendliness.
        # We'll keep columns as the dp dimension; if rows < cols, we can transpose-like iterate.
        if cols >= rows:
            dp: list[int] = [0] * cols
            total: int = 0
            for i in range(rows):
                prev: int = 0  # top-left for current cell
                for j in range(cols):
                    temp = dp[j]  # store top before overwriting
                    if matrix[i][j] == 1:
                        if j == 0:
                            dp[j] = 1
                        else:
                            dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    else:
                        dp[j] = 0
                    total += dp[j]
                    prev = temp
            return total
        else:
            # Iterate by columns outer to keep dp sized by rows if rows < cols
            dp: list[int] = [0] * rows
            total: int = 0
            for j in range(cols):
                prev: int = 0
                for i in range(rows):
                    temp = dp[i]
                    if matrix[i][j] == 1:
                        if i == 0:
                            dp[i] = 1
                        else:
                            left = dp[i - 1]
                            top = temp
                            dp[i] = 1 + min(top, left, prev)
                    else:
                        dp[i] = 0
                    total += dp[i]
                    prev = temp
            return total
