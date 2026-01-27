class Solution:
    def longestLine(self, mat: list[list[int]]) -> int:
        """Find longest line of consecutive ones in four directions using DP.

        Intuition:
            Track consecutive ones in vertical, horizontal, diagonal, and
            anti-diagonal directions separately using four DP grids.

        Approach:
            1. Create four 2D arrays for vertical, horizontal, diagonal, and
               anti-diagonal consecutive counts.
            2. For each cell with value 1, update each direction from its
               respective predecessor.
            3. Track the global maximum across all four directions.

        Complexity:
            Time: O(m * n)
            Space: O(m * n)
        """
        rows, cols = len(mat), len(mat[0])
        vertical = [[0] * (cols + 2) for _ in range(rows + 2)]
        horizontal = [[0] * (cols + 2) for _ in range(rows + 2)]
        diagonal = [[0] * (cols + 2) for _ in range(rows + 2)]
        anti_diagonal = [[0] * (cols + 2) for _ in range(rows + 2)]
        answer = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if mat[i - 1][j - 1]:
                    vertical[i][j] = vertical[i - 1][j] + 1
                    horizontal[i][j] = horizontal[i][j - 1] + 1
                    diagonal[i][j] = diagonal[i - 1][j - 1] + 1
                    anti_diagonal[i][j] = anti_diagonal[i - 1][j + 1] + 1
                    answer = max(
                        answer,
                        vertical[i][j],
                        horizontal[i][j],
                        diagonal[i][j],
                        anti_diagonal[i][j],
                    )
        return answer
