from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Find the maximum free time after rescheduling at most k meetings.
        
        Approach:
        - Sort meetings by start time
        - Calculate prefix sums of meeting durations
        - Use sliding window to find the maximum free time by considering windows of meetings
          that can be rescheduled (up to k meetings)
        - The maximum free time is the gap between the end of the last meeting and the start
          of the next meeting, minus the total duration of meetings in between that can be rescheduled
          
        Time Complexity: O(n log n) for sorting + O(n) for sliding window = O(n log n)
        Space Complexity: O(n) for prefix sum array
        """
        n = len(startTime)
        if n == 0:
            return eventTime
            
        # Combine and sort meetings by start time
        meetings = sorted(zip(startTime, endTime), key=lambda x: x[0])
        startTime = [s for s, _ in meetings]
        endTime = [e for _, e in meetings]
        
        # Calculate prefix sums of meeting durations
        total = [0] * (n + 1)
        for i in range(n):
            total[i + 1] = total[i] + (endTime[i] - startTime[i])
        
        max_free = 0
        
        # If we can reschedule all meetings, the maximum free time is the entire event time
        if k >= n:
            return eventTime
            
        # Find the maximum free time by considering windows of k consecutive meetings
        for i in range(k - 1, n):
            # Right boundary is either the event end or the start of the next meeting
            right_bound = eventTime if i == n - 1 else startTime[i + 1]
            # Left boundary is either 0 or the end of the meeting before our window
            left_bound = 0 if i == k - 1 else endTime[i - k]
            
            # Calculate the free time in this window
            current_free = right_bound - left_bound - (total[i + 1] - total[i - k + 1])
            max_free = max(max_free, current_free)
        
        return max_free
