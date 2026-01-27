from itertools import pairwise


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        """Sort and check adjacent intervals for overlap.

        Intuition:
            If no two meetings overlap, a person can attend all of them.
            After sorting by start time, just check consecutive pairs.

        Approach:
            Sort intervals by start time. Use pairwise to iterate over
            consecutive intervals and verify each pair does not overlap
            (previous end <= next start).

        Complexity:
            Time: O(n log n) for sorting
            Space: O(1) extra space
        """
        intervals.sort()
        return all(prev[1] <= curr[0] for prev, curr in pairwise(intervals))
