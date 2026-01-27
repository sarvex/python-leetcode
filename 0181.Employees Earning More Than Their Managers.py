import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """Pandas Self-Join Approach

    Intuition:
        Join the employee table with itself on managerId to compare
        each employee's salary with their manager's salary.

    Approach:
        1. Merge employee with itself using managerId -> id join.
        2. Filter rows where the employee's salary exceeds the manager's.
        3. Return the employee names in the required format.

    Complexity:
        Time: O(n) for the merge and filter
        Space: O(n) for the merged DataFrame
    """
    merged = employee.merge(
        right=employee, how="left", left_on="managerId", right_on="id"
    )
    higher_earners = merged[merged["salary_x"] > merged["salary_y"]]["name_x"]

    return pd.DataFrame({"Employee": higher_earners})
