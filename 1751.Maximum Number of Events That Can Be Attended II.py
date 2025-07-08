from typing import List


class Solution:
    """
    Solution for finding maximum value from attending at most k non-overlapping events.

    Tagline: Iterative DP with Predecessor Array for Optimal Event Scheduling

    Intuition:
    We need to select at most k non-overlapping events to maximize the total value.
    This solution uses an iterative DP approach with a predecessor array to efficiently
    find the latest non-overlapping event for each event.

    Approach:
    1. Sort events by end time to process them in chronological order
    2. Create a predecessor array to store the index of the latest non-overlapping event for each event
    3. Use a DP table where dp[j] represents the maximum value when attending at most j events
    4. For each event, decide whether to include it (using the predecessor array) or not
    5. Track the maximum value obtained for each possible number of events up to k

    Complexity:
    Time: O(n log n + nk) where n is the number of events
          - O(n log n) for sorting
          - O(n log n) for predecessor array construction
          - O(nk) for the DP computation
    Space: O(n) for the predecessor array and DP table
    """
    def maxValue(self, events: List[List[int]], k: int) -> int:
        if not events or k == 0:
            return 0

        n = len(events)
        # Sort events by end time
        events.sort(key=lambda e: e[1])

        # Precompute the predecessor for each event
        # predecessor[i] = index of the latest event that ends before events[i] starts
        events_start_sorted = [(e[0], i) for i, e in enumerate(events)]
        events_start_sorted.sort()

        predecessor = [-1] * n
        j = 0
        for start, idx in events_start_sorted:
            # Find the first event that ends after current start time
            while j < n and events[j][1] < start:
                j += 1
            predecessor[idx] = j - 1  # j-1 is the last event that ends before current starts

        # dp[i][j] = max value using first i events and at most j events
        # We'll use a 1D array and update it iteratively to save space
        dp_prev = [0] * n
        max_value = 0

        for j in range(1, k + 1):
            dp_curr = [0] * n

            for i in range(n):
                # Option 1: Don't take the current event
                dp_curr[i] = dp_curr[i - 1] if i > 0 else 0

                # Option 2: Take the current event
                prev_idx = predecessor[i]
                take_value = events[i][2]
                if j > 1 and prev_idx != -1:
                    take_value += dp_prev[prev_idx]

                dp_curr[i] = max(dp_curr[i], take_value)

            dp_prev = dp_curr
            max_value = max(max_value, dp_curr[-1] if n > 0 else 0)
        return max_value
