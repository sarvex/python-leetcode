from math import inf
from typing import List


def rotate(a: List[List[int]]) -> List[List[int]]:
    """Rotate matrix clockwise by 90 degrees.

    Approach: zip of reversed rows, then convert tuples to lists for mutability.
    Intuition: Use transpose of reversed rows to achieve 90° rotation in O(mn).
    Complexity: time O(mn), space O(mn).
    """
    return [list(row) for row in zip(*reversed(a))]


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        """Minimum sum of areas to cover all 1s with three rectangles.

        Tagline: DP over quadrants + rotations to reuse one subroutine.
        Intuition: Precompute, for any anchored submatrix, the minimal bounding-rectangle
        area that covers all 1s inside. With four orientations (via rotation), we can
        query combinations for the three-rectangle partitions efficiently.
        Approach: For a given orientation, compute `minimumArea` DP f where
        f[i+1][j+1] is the minimal bounding-rectangle area of all 1s in submatrix
        (0,0)-(i,j). Build four DP tables for four corners via rotation, then test
        valid partition lines and take the minimum.
        Complexity:
        - Time: O(mn) per orientation and per sweep; overall O(mn) with small constants.
        - Space: O(mn) for DP tables.
        """

        def f(a: List[List[int]]) -> int:
            m, n = len(a), len(a[0])

            # Precompute left/right-most 1 positions for each row.
            lr: List[tuple[int, int]] = []
            for i in range(m):
                l, r = -1, 0
                for j in range(n):
                    if a[i][j] > 0:
                        if l < 0:
                            l = j
                        r = j
                lr.append((l, r))

            def minimumArea(mat: List[List[int]]) -> List[List[int]]:
                m2, n2 = len(mat), len(mat[0])
                # f2[i+1][j+1]: minimal area covering all 1s in (0,0)-(i,j)
                f2 = [[0] * (n2 + 1) for _ in range(m2 + 1)]
                # border[j] tracks the current active top row and [l,r] span of the bounding box
                border: List[tuple[int, int, int]] = [(-1, 0, 0)] * n2
                for i2, row in enumerate(mat):
                    left, right = -1, 0
                    for j2, x in enumerate(row):
                        if x:
                            if left < 0:
                                left = j2
                            right = j2
                        pre_top, pre_left, pre_right = border[j2]
                        if left < 0:
                            # current row all zeros so far; inherit from top
                            f2[i2 + 1][j2 + 1] = f2[i2][j2 + 1]
                        elif pre_top < 0:
                            # first row that contains ones in this column block
                            f2[i2 + 1][j2 + 1] = right - left + 1
                            border[j2] = (i2, left, right)
                        else:
                            # extend previous bounding box vertically and/or horizontally
                            l2 = min(pre_left, left)
                            r2 = max(pre_right, right)
                            f2[i2 + 1][j2 + 1] = (r2 - l2 + 1) * (i2 - pre_top + 1)
                            border[j2] = (pre_top, l2, r2)
                return f2

            # lt[i+1][j+1]: minimal area for submatrix with top-left at (0,0) and bottom-right (i,j)
            lt = minimumArea(a)

            a = rotate(a)
            # lb[i][j+1]: submatrix with bottom-left at (m-1,0) and top-right at (i,j)
            lb = rotate(rotate(rotate(minimumArea(a))))

            a = rotate(a)
            # rb[i][j]: submatrix with bottom-right at (m-1,n-1) and top-left at (i,j)
            rb = rotate(rotate(minimumArea(a)))

            a = rotate(a)
            # rt[i+1][j]: submatrix with top-right at (0,n-1) and bottom-left at (i,j)
            rt = rotate(minimumArea(a))

            ans = inf
            m, n = len(lt) - 1, len(lt[0]) - 1

            # Horizontal three-stripe partition: top | middle | bottom
            if m >= 3:
                # Maintain bounding box for middle stripe efficiently
                left, right, top, bottom = n, 0, m, 0
                for i in range(1, m):
                    # expand middle stripe start at row i and grow downward
                    left, right, top, bottom = n, 0, m, 0
                    for j in range(i + 1, m):
                        l_row, r_row = lr[j - 1]
                        if l_row >= 0:
                            left = min(left, l_row)
                            right = max(right, r_row)
                            top = min(top, j - 1)
                            bottom = j - 1
                        mid_area = 0 if left > right else (right - left + 1) * (bottom - top + 1)
                        # top area from lt, bottom area from lb
                        ans = min(ans, lt[i][n] + mid_area + lb[j][n])

            # Cross and L-shaped partitions
            if m >= 2 and n >= 2:
                for i in range(1, m):
                    for j in range(1, n):
                        # top-middle-bottom (cross like): lt top-left, lb top-right, rb bottom
                        ans = min(ans, lt[i][n] + lb[i][j] + rb[i][j])
                        # left-top-right (another arrangement): lt left, rt right-top, lb bottom
                        ans = min(ans, lt[i][j] + rt[i][j] + lb[i][n])
            return ans

        # Try original and rotated grid; take the minimum.
        return min(f(grid), f(rotate(grid)))
