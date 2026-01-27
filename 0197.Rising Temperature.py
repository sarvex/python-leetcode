import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    """Pandas Diff Approach

    Intuition:
        Sort by date and use diff to find rows where temperature increased
        from the previous consecutive day.

    Approach:
        1. Sort the weather DataFrame by recordDate.
        2. Use diff on temperature and recordDate columns.
        3. Filter rows where temperature increased and date diff is exactly 1 day.

    Complexity:
        Time: O(n log n) for sorting
        Space: O(n) for the diff computations
    """
    weather.sort_values(by="recordDate", inplace=True)
    return weather[
        (weather.temperature.diff() > 0) & (weather.recordDate.diff().dt.days == 1)
    ][["id"]]
