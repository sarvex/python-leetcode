class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """In-place state encoding to simulate one step of Conway's Game of Life.

        Intuition:
            Use intermediate states (2 for alive-to-dead, -1 for dead-to-alive)
            to encode transitions without extra space, then decode in a second pass.

        Approach:
            1. For each cell, count live neighbors (values > 0 include original live cells
               and cells marked 2 that were alive).
            2. Mark live cells dying (< 2 or > 3 neighbors) as 2.
            3. Mark dead cells becoming alive (exactly 3 neighbors) as -1.
            4. Second pass: convert 2 -> 0 and -1 -> 1.

        Complexity:
            Time: O(m * n)
            Space: O(1)
        """
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                live_neighbors = -board[i][j]
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < rows and 0 <= y < cols and board[x][y] > 0:
                            live_neighbors += 1
                if board[i][j] and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = -1
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
