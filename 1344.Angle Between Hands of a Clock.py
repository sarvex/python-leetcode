class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """Calculate the smaller angle between hour and minute hands.

        Intuition:
            The hour hand moves 0.5 degrees per minute and 30 degrees per hour.
            The minute hand moves 6 degrees per minute.

        Approach:
            Compute both hand positions in degrees, take the absolute difference,
            and return the minimum of the difference and its complement to 360.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        hour_angle = 30 * hour + 0.5 * minutes
        minute_angle = 6.0 * minutes
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
