class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        """Return the number of days in the given month of the given year.

        Intuition:
            The number of days per month is fixed except for February, which
            depends on whether the year is a leap year.

        Approach:
            Precompute a lookup table of days per month. Determine leap year
            status using standard calendar rules and adjust February accordingly.

        Complexity:
            Time: O(1)
            Space: O(1) for the fixed-size lookup table
        """
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_month = [
            0,
            31,
            29 if is_leap else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,
        ]
        return days_in_month[month]
