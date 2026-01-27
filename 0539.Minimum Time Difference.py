from itertools import pairwise


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        """Sort time points as minutes and find minimum adjacent difference.

        Intuition:
            Convert times to minutes, sort them, and the minimum difference
            must be between adjacent values (including wrap-around).

        Approach:
            If more than 1440 time points, pigeonhole guarantees a duplicate.
            Convert to minutes, sort, append first + 1440 for wrap-around,
            then find minimum adjacent difference.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        if len(timePoints) > 1440:
            return 0
        minutes_sorted = sorted(
            int(time[:2]) * 60 + int(time[3:]) for time in timePoints
        )
        minutes_sorted.append(minutes_sorted[0] + 1440)
        return min(later - earlier for earlier, later in pairwise(minutes_sorted))
