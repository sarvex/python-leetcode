from itertools import accumulate


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """Check if car pooling is possible using difference array.

        Intuition:
            Model passenger count changes at each location using a difference
            array, then check if the running sum ever exceeds capacity.

        Approach:
            Create a difference array sized to the maximum destination. For each
            trip, add passengers at the pickup and subtract at the dropoff.
            Compute prefix sums and verify all values stay within capacity.

        Complexity:
            Time: O(n + m) where n is number of trips and m is max destination
            Space: O(m) for the difference array
        """
        max_location = max(trip[2] for trip in trips)
        diff = [0] * (max_location + 1)
        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers
        return all(current <= capacity for current in accumulate(diff))
