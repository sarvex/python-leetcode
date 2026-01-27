class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        """DFS to reveal cells in Minesweeper game.

        Intuition:
            If clicking a mine, mark it. Otherwise, count adjacent mines.
            If no adjacent mines, recursively reveal neighbors.

        Approach:
            On clicking an empty cell, count adjacent mines. If count > 0,
            set the digit. Otherwise, mark as blank and DFS into all
            unrevealed neighbors.

        Complexity:
            Time: O(m * n)
            Space: O(m * n) for recursion stack
        """

        def dfs(row: int, col: int) -> None:
            mine_count = 0
            for x in range(row - 1, row + 2):
                for y in range(col - 1, col + 2):
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] == "M":
                        mine_count += 1
            if mine_count:
                board[row][col] = str(mine_count)
            else:
                board[row][col] = "B"
                for x in range(row - 1, row + 2):
                    for y in range(col - 1, col + 2):
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] == "E":
                            dfs(x, y)

        rows, cols = len(board), len(board[0])
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        else:
            dfs(i, j)
        return board
