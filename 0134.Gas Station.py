from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """One-pass greedy algorithm with two pointers

        Intuition: If we can't reach a station from the starting point, then all stations
        between the starting point and that station can't be the starting point either.

        Approach: Use two pointers to track potential starting station and current station.
        We accumulate the difference between gas and cost. If at any point the sum becomes
        negative, we move the potential starting station backwards and continue.

        Complexity:
        Time: O(n) where n is the number of gas stations
        Space: O(1) constant extra space
        """
        n = len(gas)
        start = end = n - 1  # Start from the last station
        surplus = visited = 0

        while visited < n:
            # Add the surplus/deficit at the current station
            surplus += gas[end] - cost[end]
            visited += 1
            end = (end + 1) % n  # Move to next station circularly

            # If we're running on deficit, move starting point backwards
            while surplus < 0 and visited < n:
                start -= 1
                surplus += gas[start] - cost[start]
                visited += 1

        # If final total_surplus is negative, no solution exists
        return -1 if surplus < 0 else start
