class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Monotonic Stack Approach

        Intuition:
            For each bar, find the nearest shorter bar on the left and right
            to determine the maximum rectangle width with that bar's height.

        Approach:
            Use a monotonic increasing stack. As we iterate, pop bars that
            are taller than the current bar, recording the current index as
            their right boundary. The top of the remaining stack gives the
            left boundary. Compute the area for each bar using these boundaries.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        num_bars = len(heights)
        stack: list[int] = []
        left_boundary = [-1] * num_bars
        right_boundary = [num_bars] * num_bars
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                right_boundary[stack[-1]] = i
                stack.pop()
            if stack:
                left_boundary[i] = stack[-1]
            stack.append(i)
        return max(
            height * (right_boundary[i] - left_boundary[i] - 1)
            for i, height in enumerate(heights)
        )
