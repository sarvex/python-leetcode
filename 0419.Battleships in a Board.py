class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        """Count battleship heads by checking no predecessor above or left.

        Intuition:
            A battleship occupies consecutive cells horizontally or vertically.
            Only count the top-left cell of each battleship to avoid duplicates.

        Approach:
            1. Iterate through every cell in the board.
            2. Skip empty cells ('.').
            3. Skip cells with an 'X' directly above or to the left.
            4. Count the remaining 'X' cells as battleship starts.

        Complexity:
            Time: O(m * n) where m and n are board dimensions.
            Space: O(1) using only a counter variable.
        """
        num_rows, num_cols = len(board), len(board[0])
        count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == ".":
                    continue
                if row > 0 and board[row - 1][col] == "X":
                    continue
                if col > 0 and board[row][col - 1] == "X":
                    continue
                count += 1
        return count
