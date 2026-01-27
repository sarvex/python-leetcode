from itertools import pairwise


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """Track alternating comparison streaks for longest turbulent subarray.

        Intuition:
        A turbulent subarray alternates between increasing and decreasing.
        Track two streak lengths: one ending with an increase, one with a
        decrease, and swap them at each step.

        Approach:
        1. Maintain two counters: increasing_streak and decreasing_streak
        2. For each adjacent pair, extend the opposite streak + 1 or reset to 1
        3. Track the maximum of both streaks

        Complexity:
        Time: O(n) where n is the array length
        Space: O(1)
        """
        max_length = increasing_streak = decreasing_streak = 1
        for prev, curr in pairwise(arr):
            new_increasing = decreasing_streak + 1 if prev < curr else 1
            new_decreasing = increasing_streak + 1 if prev > curr else 1
            increasing_streak, decreasing_streak = new_increasing, new_decreasing
            max_length = max(max_length, increasing_streak, decreasing_streak)
        return max_length
