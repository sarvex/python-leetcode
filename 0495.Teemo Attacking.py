from itertools import pairwise


class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        """Calculate total poisoned time by merging overlapping intervals.

        Intuition:
            Each attack poisons for `duration` seconds, but consecutive attacks
            may overlap. We only add the non-overlapping portion for each pair.

        Approach:
            Start with one full duration for the last attack. For each consecutive
            pair of attacks, add the minimum of the duration and the gap between them.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        total_time = duration
        for start, next_start in pairwise(timeSeries):
            total_time += min(duration, next_start - start)
        return total_time
