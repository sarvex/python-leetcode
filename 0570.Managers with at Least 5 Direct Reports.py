import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """Find managers with at least five direct reports using groupby and merge.

    Intuition:
        Count the number of employees reporting to each manager and filter
        for those with five or more reports.

    Approach:
        1. Group employees by managerId and count direct reports.
        2. Filter for managers with at least 5 reports.
        3. Merge back with the employee table to get manager names.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    manager_report_count = (
        employee.groupby("managerId").size().reset_index(name="directReports")
    )

    result = manager_report_count[manager_report_count["directReports"] >= 5]

    result = result.merge(
        employee[["id", "name"]], left_on="managerId", right_on="id", how="inner"
    )

    result = result[["name"]]

    return result
