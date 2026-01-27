class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        """Find minimum number of taps to water the entire garden [0, n].

        Intuition:
            Transform each tap's range into an interval and reduce to a
            jump game / interval covering problem.

        Approach:
            For each tap, record the farthest right it can reach from its
            leftmost point. Then greedily extend coverage using the jump
            game approach: track current boundary and next reachable boundary.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        farthest = [0] * (n + 1)
        for i, reach in enumerate(ranges):
            left = max(0, i - reach)
            farthest[left] = max(farthest[left], i + reach)

        taps_used = current_end = next_end = 0
        for i in range(n):
            next_end = max(next_end, farthest[i])
            if next_end <= i:
                return -1
            if current_end == i:
                taps_used += 1
                current_end = next_end
        return taps_used
