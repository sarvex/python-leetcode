from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Union-Find (Disjoint Set) based Approach

        Intuition:
        We can model the problem using a Union-Find data structure where each day points to the next
        available day. This helps us efficiently find the earliest available day to attend an event.

        Approach:
        1. Sort events by their end day (earlier end days first)
        2. Use Union-Find to track and update the next available day
        3. For each event, find the earliest available day between its start and end days
        4. If a valid day is found, mark it as used and update the Union-Find structure

        Complexity:
        Time: O(E α(D)) where E is the number of events and D is the range of days,
              α is the inverse Ackermann function (effectively constant)
        Space: O(D) where D is the maximum end day
        """
        # Sort events by end day to process events that end earlier first
        events.sort(key=lambda e: e[1])

        # Find the maximum end day to initialize the Union-Find array
        max_day = events[-1][1] if events else 0

        # Initialize Union-Find array where parent[i] points to the next available day
        parent = list(range(max_day + 2))  # +2 to handle 1-based indexing and edge cases

        def find(x: int) -> int:
            """Find the root parent of x with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        events_attended = 0

        for start, end in events:
            # Find the earliest available day >= start
            available_day = find(start)

            # If we found an available day before or on the end day
            if available_day <= end:
                events_attended += 1
                # Mark this day as used by pointing to the next day
                parent[available_day] = available_day + 1

        return events_attended
