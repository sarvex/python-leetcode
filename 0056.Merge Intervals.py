from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge overlapping intervals.

        Intuition:
        Sort intervals by start time and then merge overlapping intervals by tracking
        the current merged interval's end time.

        Approach:
        1. Sort intervals by their start time
        2. Initialize the first interval as the current merged interval
        3. For each subsequent interval:
           - If it doesn't overlap with current merged interval, add current to result
             and update current to this new interval
           - If it overlaps, extend the end of current merged interval if needed
        4. Add the final merged interval to the result

        Complexity:
        Time: O(n log n) due to sorting
        Space: O(n) for the result array (not counting the input)
        """
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort()

        result = []
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if current_end < start:
                # No overlap, add current interval to result
                result.append([current_start, current_end])
                # Update current interval
                current_start, current_end = start, end
            else:
                # Overlap found, extend current interval if needed
                current_end = max(current_end, end)

        # Add the final merged interval
        result.append([current_start, current_end])
        return result
