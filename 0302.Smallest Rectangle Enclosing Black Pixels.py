class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        """Binary search on rows and columns to find bounding rectangle.

        Intuition:
            Since we know a black pixel exists, we can binary search for the
            top, bottom, left, and right boundaries of the black pixel region.

        Approach:
            1. Binary search for the topmost row containing a black pixel.
            2. Binary search for the bottommost row containing a black pixel.
            3. Binary search for the leftmost column containing a black pixel.
            4. Binary search for the rightmost column containing a black pixel.
            5. Return the area of the bounding rectangle.

        Complexity:
            Time: O(m * log(n) + n * log(m)) where m is rows and n is columns
            Space: O(1)
        """
        rows, cols = len(image), len(image[0])

        left, right = 0, x
        while left < right:
            mid = (left + right) >> 1
            col = 0
            while col < cols and image[mid][col] == "0":
                col += 1
            if col < cols:
                right = mid
            else:
                left = mid + 1
        top = left

        left, right = x, rows - 1
        while left < right:
            mid = (left + right + 1) >> 1
            col = 0
            while col < cols and image[mid][col] == "0":
                col += 1
            if col < cols:
                left = mid
            else:
                right = mid - 1
        bottom = left

        left, right = 0, y
        while left < right:
            mid = (left + right) >> 1
            row = 0
            while row < rows and image[row][mid] == "0":
                row += 1
            if row < rows:
                right = mid
            else:
                left = mid + 1
        left_bound = left

        left, right = y, cols - 1
        while left < right:
            mid = (left + right + 1) >> 1
            row = 0
            while row < rows and image[row][mid] == "0":
                row += 1
            if row < rows:
                left = mid
            else:
                right = mid - 1
        right_bound = left

        return (bottom - top + 1) * (right_bound - left_bound + 1)
