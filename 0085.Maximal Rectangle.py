class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """Histogram-Based Approach

        Intuition:
            Treat each row as the base of a histogram where bar heights
            are the count of consecutive '1's above (including the row).
            Then solve largest rectangle in histogram for each row.

        Approach:
            Build a heights array incrementally row by row. For each row,
            if the cell is '1', increase the height; otherwise reset to 0.
            Apply the largest rectangle in histogram algorithm to each row's
            heights and track the maximum area.

        Complexity:
            Time: O(m * n) where m is rows and n is columns
            Space: O(n)
        """
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for j, val in enumerate(row):
                if val == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self._largest_rectangle_area(heights))
        return max_area

    def _largest_rectangle_area(self, heights: list[int]) -> int:
        """Compute the largest rectangle area in a histogram using monotonic stack."""
        num_bars = len(heights)
        stack: list[int] = []
        left_boundary = [-1] * num_bars
        right_boundary = [num_bars] * num_bars
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                left_boundary[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(num_bars - 1, -1, -1):
            height = heights[i]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                right_boundary[i] = stack[-1]
            stack.append(i)
        return max(
            height * (right_boundary[i] - left_boundary[i] - 1)
            for i, height in enumerate(heights)
        )
