import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    """Pandas GroupBy Transform Approach

    Intuition:
        Merge employees with departments, then use groupby transform
        to find the max salary per department and filter matching rows.

    Approach:
        1. Merge employee and department tables on departmentId.
        2. Compute the maximum salary per department using transform.
        3. Filter employees whose salary equals the department maximum.
        4. Select and rename columns to match the required output.

    Complexity:
        Time: O(n) for merge and groupby transform
        Space: O(n) for the merged DataFrame
    """
    merged = employee.merge(department, left_on="departmentId", right_on="id")

    max_salaries = merged.groupby("departmentId")["salary"].transform("max")

    top_earners = merged[merged["salary"] == max_salaries]

    result = top_earners[["name_y", "name_x", "salary"]].copy()
    result.columns = ["Department", "Employee", "Salary"]

    return result
