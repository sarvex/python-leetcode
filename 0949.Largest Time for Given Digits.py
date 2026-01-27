class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        """Brute-force enumerate all valid times from largest to smallest.

        Intuition:
            With only 4 digits and time constraints (0-23 hours, 0-59 minutes),
            iterate from the largest possible time downward and check if the
            digit distribution matches.

        Approach:
            1. Count digit frequencies in the input array.
            2. Iterate hours from 23 down to 0, minutes from 59 down to 0.
            3. For each candidate time, compute its digit frequency.
            4. Return the first match found.

        Complexity:
            Time: O(1) — at most 24 * 60 = 1440 iterations with constant work
            Space: O(1) — fixed-size digit count arrays
        """
        digit_count = [0] * 10
        for digit in arr:
            digit_count[digit] += 1
        for hour in range(23, -1, -1):
            for minute in range(59, -1, -1):
                candidate = [0] * 10
                candidate[hour // 10] += 1
                candidate[hour % 10] += 1
                candidate[minute // 10] += 1
                candidate[minute % 10] += 1
                if digit_count == candidate:
                    return f"{hour:02}:{minute:02}"
        return ""
