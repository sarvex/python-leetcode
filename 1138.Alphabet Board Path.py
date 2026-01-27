class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """Return the path to spell the target on a 5x6 alphabet board.

        Intuition:
            The board has 'z' isolated at position (5,0). Moving left/up
            before right/down avoids going out of bounds near 'z'.

        Approach:
            Track the current row and column. For each target character,
            compute the destination position and move left/up first, then
            right/down, to safely navigate around the board's edge.

        Complexity:
            Time: O(n * 5) where n is the length of target (max 5 moves per char)
            Space: O(n) for the result
        """
        current_row = 0
        current_col = 0
        path: list[str] = []
        for char in target:
            position = ord(char) - ord("a")
            target_row, target_col = position // 5, position % 5
            while current_col > target_col:
                current_col -= 1
                path.append("L")
            while current_row > target_row:
                current_row -= 1
                path.append("U")
            while current_col < target_col:
                current_col += 1
                path.append("R")
            while current_row < target_row:
                current_row += 1
                path.append("D")
            path.append("!")
        return "".join(path)
