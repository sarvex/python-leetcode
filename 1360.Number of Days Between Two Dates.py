class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """Calculate the number of days between two dates.

        Intuition:
            Convert each date to an absolute day count from a fixed epoch and
            return the absolute difference.

        Approach:
            Define helper functions to check leap years and compute days in
            each month. Convert each date to total days since a reference year
            (1971) by summing full years, full months, and remaining days.

        Complexity:
            Time: O(y) where y is the year difference from epoch.
            Space: O(1)
        """

        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_in_month(year: int, month: int) -> int:
            days_per_month = [
                31,
                28 + int(is_leap_year(year)),
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
            return days_per_month[month - 1]

        def total_days(date: str) -> int:
            year, month, day = map(int, date.split("-"))
            days = 0
            for y in range(1971, year):
                days += 365 + int(is_leap_year(y))
            for m in range(1, month):
                days += days_in_month(year, m)
            days += day
            return days

        return abs(total_days(date1) - total_days(date2))
