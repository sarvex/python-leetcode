class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        """Count intervals that are not covered by any other interval.

        Intuition:
            Sort by start ascending and end descending so that for equal starts,
            the wider interval comes first, making coverage detection a simple
            comparison of endpoints.

        Approach:
            Sort intervals by (start, -end). Iterate and track the previous
            non-covered interval. An interval is not covered if its end exceeds
            the previous interval's end.

        Complexity:
            Time: O(n log n)
            Space: O(1)
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 1
        previous = intervals[0]
        for interval in intervals[1:]:
            if previous[1] < interval[1]:
                count += 1
                previous = interval
        return count
