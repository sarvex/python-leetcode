class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        """Find maximum score and number of paths from bottom-right to top-left.

        Intuition:
            Work backwards from the bottom-right corner, propagating the maximum
            score and counting paths that achieve it.

        Approach:
            Use two DP grids: one for maximum score and one for path count.
            For each cell, update from right, below, and diagonal neighbors.
            Cells marked 'X' are obstacles. Return score and count modulo 10^9+7.

        Complexity:
            Time: O(n^2)
            Space: O(n^2)
        """

        def update(row: int, col: int, from_row: int, from_col: int) -> None:
            if (
                from_row >= size
                or from_col >= size
                or score[from_row][from_col] == -1
                or board[row][col] in "XS"
            ):
                return
            if score[from_row][from_col] > score[row][col]:
                score[row][col] = score[from_row][from_col]
                count[row][col] = count[from_row][from_col]
            elif score[from_row][from_col] == score[row][col]:
                count[row][col] += count[from_row][from_col]

        size = len(board)
        score = [[-1] * size for _ in range(size)]
        count = [[0] * size for _ in range(size)]
        score[-1][-1], count[-1][-1] = 0, 1

        for row in range(size - 1, -1, -1):
            for col in range(size - 1, -1, -1):
                update(row, col, row + 1, col)
                update(row, col, row, col + 1)
                update(row, col, row + 1, col + 1)
                if score[row][col] != -1 and board[row][col].isdigit():
                    score[row][col] += int(board[row][col])

        modulo = 10**9 + 7
        return [0, 0] if score[0][0] == -1 else [score[0][0], count[0][0] % modulo]
