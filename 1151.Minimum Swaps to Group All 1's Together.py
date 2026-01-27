class Solution:
    def minSwaps(self, data: list[int]) -> int:
        """Minimum swaps to group all 1s together using sliding window.

        Intuition:
            The window size equals the total count of 1s. We want to find the
            window that already contains the maximum number of 1s, minimizing swaps.

        Approach:
            Count total 1s as window size k. Slide a window of size k across the
            array, tracking the maximum number of 1s in any window. The answer is
            k minus that maximum.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        window_size = data.count(1)
        max_ones = current_ones = sum(data[:window_size])
        for i in range(window_size, len(data)):
            current_ones += data[i]
            current_ones -= data[i - window_size]
            max_ones = max(max_ones, current_ones)
        return window_size - max_ones
