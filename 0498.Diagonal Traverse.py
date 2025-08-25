class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """Diagonal traversal with alternating reversal

        Intuition:
        Traverse the matrix by enumerating each diagonal (constant i+j). Elements on
        the same diagonal can be collected by moving down-left. To match the zigzag
        order, reverse every even-indexed diagonal.

        Approach:
        - There are m+n-1 diagonals indexed by d in [0, m+n-2].
        - For each d, start at row=max(0, d-(n-1)) and col=min(d, n-1), move while
          within bounds collecting values.
        - Reverse the collected list when d is even, then append to the result.

        Complexity:
        - Time: O(m*n) — each cell is visited exactly once.
        - Space: O(1) extra (excluding output), O(min(m,n)) temporary per diagonal.
        """
        m, n = len(mat), len(mat[0])
        res: List[int] = []
        for d in range(m + n - 1):
            diag_vals: List[int] = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c >= 0:
                diag_vals.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                diag_vals.reverse()
            res.extend(diag_vals)
        return res
