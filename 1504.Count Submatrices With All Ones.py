class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        """Monotonic stack over histogram heights to count all-ones submatrices.

        Intuition:
            Treat each row as the base of a histogram of consecutive 1s heights.
            For each row, the number of all-ones submatrices ending at that row is the
            sum of minimal heights over all subarrays, computable via a monotonic stack.

        Approach:
            - Maintain `heights[j]` as the consecutive ones up to current row for column j.
            - For each row, compute contributions using a monotonic nondecreasing stack:
              let `subs[i]` be total submatrices ending at column i; when popping, we
              ensure current bar becomes the limiting height.
            - Sum per-row contributions to get the final answer.

        Complexity:
            Time: O(m*n)
            Space: O(n)
        """

        m: int = len(mat)
        n: int = len(mat[0]) if m else 0
        if m == 0 or n == 0:
            return 0

        heights: list[int] = [0] * n
        result: int = 0

        def count_row(h: list[int]) -> int:
            """Count submatrices for one histogram row using a monotonic stack."""
            stack: list[int] = []  # indices with increasing heights
            subs: list[int] = [0] * len(h)
            total: int = 0
            for i, val in enumerate(h):
                while stack and h[stack[-1]] >= val:
                    stack.pop()
                if stack:
                    left = stack[-1]
                    subs[i] = subs[left] + val * (i - left)
                else:
                    subs[i] = val * (i + 1)
                stack.append(i)
                total += subs[i]
            return total

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            result += count_row(heights)

        return result
