class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Greedy skyline scan after sorting by x asc and y desc

        Intuition:
        Sort by x increasing and y decreasing so that a right candidate is valid
        iff its y is <= current y1 and strictly greater than any y seen in this sweep.

        Approach:
        For each left point, sweep rightward and count y2 values that form a
        strictly increasing sequence up to y1.

        Complexity:
        Time: O(n log n) for sort + O(n^2) sweep
        Space: O(1) extra
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = float("-inf")
            for _, y2 in points[i + 1 :]:
                if max_y < y2 <= y1:
                    max_y = y2
                    ans += 1
        return ans
