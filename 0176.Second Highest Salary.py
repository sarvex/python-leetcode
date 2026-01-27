import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Pandas Aggregation Approach

    Intuition:
        Find the second largest unique salary by deduplicating and
        selecting the second element from a sorted descending list.

    Approach:
        1. Drop duplicate salary values to get unique salaries.
        2. Use nlargest(2) to get the top two salaries.
        3. If fewer than two unique salaries exist, return None.
        4. Otherwise return the second highest in a DataFrame.

    Complexity:
        Time: O(n log n) for sorting unique salaries
        Space: O(n) for storing unique salaries
    """
    unique_salaries = employee["salary"].drop_duplicates()

    second_highest = (
        unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    )

    if second_highest is None:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    return pd.DataFrame({"SecondHighestSalary": [second_highest]})
