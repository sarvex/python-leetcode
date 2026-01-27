import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """Return the day of the week for a given date.

        Intuition:
            Python's datetime module can directly compute the day of the week
            for any valid calendar date.

        Approach:
            Construct a date object and use strftime to get the full weekday name.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return datetime.date(year, month, day).strftime("%A")
