from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy approach using end-point sorting

        Intuition:
        Sort intervals by end time and greedily select non-overlapping intervals.
        By picking intervals that end earlier, we maximize the number of intervals we can keep.

        Approach:
        1. Sort intervals by their end times
        2. Keep track of the end time of the last selected interval
        3. For each interval, if it doesn't overlap with the last selected one, select it
        4. Otherwise, count it as an interval to be removed

        Complexity:
        Time: O(n log n) where n is the number of intervals (dominated by sorting)
        Space: O(1) excluding the input and sorting space
        """
        if not intervals:
            return 0

        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        removal_count = 0
        last_end_time = intervals[0][1]

        # Process remaining intervals
        for start, end in intervals[1:]:
            if start >= last_end_time:
                # No overlap, can keep this interval
                last_end_time = end
            else:
                # Overlap detected, need to remove this interval
                removal_count += 1

        return removal_count
