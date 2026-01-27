from bisect import bisect


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        """DP with binary search over sorted events for max k-event value.

        Intuition:
            Sort events by end time and use DP layers for each allowed
            attendance count, binary searching for compatible prior events.

        Approach:
            1. Sort events by end time.
            2. Maintain a DP array per attendance layer, storing (end_time, max_value).
            3. For each event in each layer, binary search for the latest
               non-overlapping event and update the DP if value improves.

        Complexity:
            Time: O(k * n * log n)
            Space: O(n)
        """
        events.sort(key=lambda event: event[1])
        dp = [[0, 0]]
        dp_next = [[0, 0]]
        for _ in range(k):
            for start, end, value in events:
                index = bisect(dp, [start]) - 1
                if dp[index][1] + value > dp_next[-1][1]:
                    dp_next.append([end, dp[index][1] + value])
            dp = dp_next
            dp_next = [[0, 0]]
        return dp[-1][-1]
