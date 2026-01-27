class Solution:
    def dayOfYear(self, date: str) -> int:
        """Calculate the day number of the year for a given date.

        Intuition:
            Sum up the days of all preceding months and add the current day,
            accounting for leap years in February.

        Approach:
            Parse year, month, day from the date string. Determine February
            length based on leap year rules. Sum days of months before the
            current month and add the day.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        year, month, day = (int(part) for part in date.split("-"))
        february_days = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100) else 28
        days_in_month = [31, february_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_in_month[: month - 1]) + day
