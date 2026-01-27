from itertools import pairwise


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Sorting with Pairwise Comparison Approach

        Intuition:
            After sorting, consecutive elements that form a sequence will be
            adjacent. We can scan pairs to find the longest run of consecutive
            values, skipping duplicates.

        Approach:
            Sort the array. Use pairwise iteration to compare adjacent elements.
            Skip duplicates, extend the current streak for consecutive pairs, and
            reset otherwise. Track the maximum streak length.

        Complexity:
            Time: O(n log n) due to sorting
            Space: O(1) excluding the sort space
        """
        length = len(nums)
        if length < 2:
            return length
        nums.sort()
        max_streak = current_streak = 1
        for prev_val, curr_val in pairwise(nums):
            if prev_val == curr_val:
                continue
            if prev_val + 1 == curr_val:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        return max_streak
