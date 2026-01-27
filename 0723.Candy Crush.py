class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        """Simulate candy crush by marking, crushing, and applying gravity.

        Intuition:
            Repeatedly find groups of 3+ identical candies in rows and columns,
            mark them for removal, then apply gravity to drop remaining candies.

        Approach:
            1. Scan all rows for 3+ consecutive identical values, mark with negation.
            2. Scan all columns similarly.
            3. If any candy was marked, apply gravity by shifting positive values
               down in each column and filling zeros on top.
            4. Repeat until no more candies are marked.

        Complexity:
            Time: O((m * n)^2) worst case for repeated passes
            Space: O(1) in-place modification
        """
        rows, cols = len(board), len(board[0])
        has_crush = True
        while has_crush:
            has_crush = False
            for i in range(rows):
                for j in range(2, cols):
                    if board[i][j] and abs(board[i][j]) == abs(board[i][j - 1]) == abs(
                        board[i][j - 2]
                    ):
                        has_crush = True
                        board[i][j] = board[i][j - 1] = board[i][j - 2] = -abs(
                            board[i][j]
                        )
            for j in range(cols):
                for i in range(2, rows):
                    if board[i][j] and abs(board[i][j]) == abs(board[i - 1][j]) == abs(
                        board[i - 2][j]
                    ):
                        has_crush = True
                        board[i][j] = board[i - 1][j] = board[i - 2][j] = -abs(
                            board[i][j]
                        )
            if has_crush:
                for j in range(cols):
                    write_pos = rows - 1
                    for i in range(rows - 1, -1, -1):
                        if board[i][j] > 0:
                            board[write_pos][j] = board[i][j]
                            write_pos -= 1
                    while write_pos >= 0:
                        board[write_pos][j] = 0
                        write_pos -= 1
        return board
