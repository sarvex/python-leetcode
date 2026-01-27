class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """Greedy selection of rightmost points to cover all intervals.

        Intuition:
            Sorting by right endpoint and greedily picking the rightmost
            possible points minimizes the total set size while ensuring
            every interval contains at least two chosen points.

        Approach:
            1. Sort intervals by right endpoint ascending, then by left
               endpoint descending.
            2. Track the two largest selected points (second_last, last).
            3. For each interval, if second_last is inside, skip. If only
               last is outside, add one point. Otherwise add two points.

        Complexity:
            Time: O(N log N)
            Space: O(1)
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        second_last = last = -1
        result = 0
        for start, end in intervals:
            if start <= second_last:
                continue
            if start > last:
                result += 2
                second_last, last = end - 1, end
            else:
                result += 1
                second_last, last = last, end
        return result
