class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Flattened Binary Search Approach

        Intuition:
            The matrix rows are sorted and each row starts greater than
            the previous row's end, so the entire matrix can be treated
            as a single sorted array.

        Approach:
            Map a 1D index to 2D coordinates using divmod. Perform standard
            binary search on the flattened index range [0, m*n - 1].

        Complexity:
            Time: O(log(m * n))
            Space: O(1)
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        left, right = 0, num_rows * num_cols - 1
        while left < right:
            mid = (left + right) >> 1
            row, col = divmod(mid, num_cols)
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // num_cols][left % num_cols] == target
