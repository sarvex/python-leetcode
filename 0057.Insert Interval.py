from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Linear scan approach - Insert a new interval into a sorted list of non-overlapping intervals

        Intuition:
        Since the input intervals are already sorted and non-overlapping, we can perform a linear scan
        to find the correct position for the new interval without sorting the entire list again.

        Approach:
        1. Initialize an empty result list
        2. Process intervals that come before the new interval (end < newStart)
        3. Merge overlapping intervals with the new interval
        4. Add the merged new interval to the result
        5. Add remaining intervals that come after the new interval

        Complexity:
        Time: O(n) where n is the number of intervals
        Space: O(n) for the result list
        """
        result = []
        i, n = 0, len(intervals)

        # Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
