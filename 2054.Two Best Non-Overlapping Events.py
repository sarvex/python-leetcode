from typing import List
from bisect import bisect_right


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events based on start time
        events.sort()

        n = len(events)
        # max_value_suffix[i] will store the maximum value of an event starting at or after index i
        max_value_suffix = [0] * n
        max_value_suffix[-1] = events[-1][2]

        for i in range(n - 2, -1, -1):
            max_value_suffix[i] = max(events[i][2], max_value_suffix[i + 1])

        ans = 0
        for _, end, value in events:
            # Find the first event that starts strictly after the current event ends
            idx = bisect_right(events, end, key=lambda x: x[0])

            # If such an event exists, add its maximum possible value (from suffix array)
            if idx < n:
                value += max_value_suffix[idx]

            ans = max(ans, value)

        return ans
