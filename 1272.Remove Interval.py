class Solution:
    def removeInterval(
        self, intervals: list[list[int]], toBeRemoved: list[int]
    ) -> list[list[int]]:
        """Remove an interval from a set of disjoint intervals.

        Intuition:
            Each existing interval either does not overlap with the removal
            interval, or gets split into up to two parts.

        Approach:
            For each interval, if it does not overlap with the removal range,
            keep it as is. Otherwise, keep the portions that fall outside the
            removal range (left part before removal start, right part after
            removal end).

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        remove_start, remove_end = toBeRemoved
        result: list[list[int]] = []
        for start, end in intervals:
            if start >= remove_end or end <= remove_start:
                result.append([start, end])
            else:
                if start < remove_start:
                    result.append([start, remove_start])
                if end > remove_end:
                    result.append([remove_end, end])
        return result
