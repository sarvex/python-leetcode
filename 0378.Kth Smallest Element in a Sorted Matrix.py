class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        """Find kth smallest element in sorted matrix using binary search on value.

        Intuition:
            The matrix is sorted row-wise and column-wise. Binary search on the
            value range and count elements less than or equal to the mid value.

        Approach:
            Binary search between the smallest (top-left) and largest (bottom-right)
            elements. For each mid value, count elements <= mid by starting from
            the bottom-left corner and moving right when the value is <= mid or
            up when it exceeds mid. Narrow the search range based on the count.

        Complexity:
            Time: O(n * log(max - min))
            Space: O(1)
        """

        def count_no_greater_than(mid: int) -> bool:
            count = 0
            row, col = size - 1, 0
            while row >= 0 and col < size:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count >= k

        size = len(matrix)
        left, right = matrix[0][0], matrix[size - 1][size - 1]
        while left < right:
            mid = (left + right) >> 1
            if count_no_greater_than(mid):
                right = mid
            else:
                left = mid + 1
        return left
