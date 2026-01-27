class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        """Enumerate all valid times by counting set bits.

        Intuition:
            A binary watch has 10 LEDs (4 for hours, 6 for minutes).
            We can enumerate all possible hour/minute combinations and
            check if the total number of set bits matches turnedOn.

        Approach:
            1. Iterate over all hours (0-11) and minutes (0-59).
            2. Count the combined set bits in hour and minute values.
            3. Include the time if the bit count equals turnedOn.

        Complexity:
            Time: O(1) since the iteration space is fixed (12 * 60 = 720)
            Space: O(1) excluding the output list
        """
        return [
            f"{hour:d}:{minute:02d}"
            for hour in range(12)
            for minute in range(60)
            if (bin(hour) + bin(minute)).count("1") == turnedOn
        ]
