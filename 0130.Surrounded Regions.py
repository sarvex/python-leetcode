from itertools import pairwise


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """Border DFS Marking Approach

        Intuition:
            Only 'O' cells connected to the border cannot be captured. Mark all
            border-connected 'O' cells first, then flip remaining 'O' cells to 'X'
            and restore marked cells back to 'O'.

        Approach:
            DFS from all border 'O' cells, marking them with a temporary character.
            Then iterate through the board: restore temporary marks to 'O' and flip
            any remaining 'O' to 'X'.

        Complexity:
            Time: O(m * n) where m and n are board dimensions
            Space: O(m * n) for the recursion stack in worst case
        """

        def dfs(row: int, col: int) -> None:
            if not (0 <= row < rows and 0 <= col < cols and board[row][col] == "O"):
                return
            board[row][col] = "."
            for delta_r, delta_c in pairwise((-1, 0, 1, 0, -1)):
                dfs(row + delta_r, col + delta_c)

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
