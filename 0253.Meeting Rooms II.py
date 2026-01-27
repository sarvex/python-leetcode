from itertools import accumulate


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """Sweep line with prefix sums to find peak concurrent meetings.

        Intuition:
            Each meeting adds one to the room count at its start and removes
            one at its end. The maximum prefix sum is the peak room usage.

        Approach:
            Create a delta array. For each interval, increment at start and
            decrement at end. Compute prefix sums and return the maximum,
            which represents the most concurrent meetings.

        Complexity:
            Time: O(n + T) where T is the time range
            Space: O(T) for the delta array
        """
        delta = [0] * 1000010
        for start, end in intervals:
            delta[start] += 1
            delta[end] -= 1
        return max(accumulate(delta))
