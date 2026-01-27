from bisect import bisect_left
from math import inf


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        """Binary search on sorted start points to find the right interval.

        Intuition:
            For each interval's end point, we need the smallest start point
            that is >= end. Sorting intervals by start point allows binary search.

        Approach:
            1. Create a sorted array of (start, original_index) pairs.
            2. For each interval, binary search for its end point in the sorted
               starts array.
            3. If found within bounds, record the original index; otherwise -1.

        Complexity:
            Time: O(n log n) for sorting and n binary searches.
            Space: O(n) for the sorted array and result.
        """
        num_intervals = len(intervals)
        result = [-1] * num_intervals
        sorted_starts = sorted((start, idx) for idx, (start, _) in enumerate(intervals))
        for idx, (_, end) in enumerate(intervals):
            position = bisect_left(sorted_starts, (end, -inf))
            if position < num_intervals:
                result[idx] = sorted_starts[position][1]
        return result
