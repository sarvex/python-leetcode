from itertools import accumulate


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        """Return the total number of seats reserved for each flight.

        Intuition:
            Instead of updating every flight in a range, use a difference array
            to mark the start and end of each booking efficiently.

        Approach:
            Build a difference array where each booking adds seats at the start
            index and subtracts at the index after the end. Then compute the
            prefix sum to get the final seat counts.

        Complexity:
            Time: O(n + m) where m is the number of bookings
            Space: O(n) for the difference array
        """
        diff = [0] * n
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        return list(accumulate(diff))
