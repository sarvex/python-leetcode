from itertools import pairwise


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        """DFS flood fill from starting pixel to connected same-color region.

        Intuition:
            Starting from the given pixel, recursively paint all connected
            pixels that share the original color with the new color.

        Approach:
            1. Record the original color at (sr, sc).
            2. DFS to all 4-directionally adjacent pixels with the same
               original color, painting them with the new color.
            3. Skip pixels already painted with the new color to avoid cycles.

        Complexity:
            Time: O(m * n) where m, n are image dimensions
            Space: O(m * n) for recursion stack in worst case
        """

        def dfs(row: int, col: int) -> None:
            if (
                not 0 <= row < rows
                or not 0 <= col < cols
                or image[row][col] != original_color
                or image[row][col] == color
            ):
                return
            image[row][col] = color
            for delta_row, delta_col in pairwise(directions):
                dfs(row + delta_row, col + delta_col)

        directions = (-1, 0, 1, 0, -1)
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        dfs(sr, sc)
        return image
