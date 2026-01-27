import numpy as np
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Pandas Sorting Approach

    Intuition:
        Extract unique salaries, sort descending, and pick the Nth element.

    Approach:
        1. Get unique salary values from the DataFrame.
        2. If fewer than N unique salaries exist, return NaN.
        3. Otherwise sort descending and select the (N-1)th index element.

    Complexity:
        Time: O(n log n) for sorting unique salaries
        Space: O(n) for storing unique salaries
    """
    unique_salaries = employee.salary.unique()
    if len(unique_salaries) < N:
        return pd.DataFrame([np.NaN], columns=[f"getNthHighestSalary({N})"])
    else:
        salary = sorted(unique_salaries, reverse=True)[N - 1]
        return pd.DataFrame([salary], columns=[f"getNthHighestSalary({N})"])
