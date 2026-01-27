import pandas as pd


def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    """Pandas GroupBy NLargest Approach

    Intuition:
        Find the top three distinct salaries per department and filter
        employees earning at or above the cutoff salary.

    Approach:
        1. Deduplicate salary-department pairs and find the top 3 salaries per dept.
        2. Compute the minimum of those top 3 as the cutoff per department.
        3. Map department names and cutoffs to each employee row.
        4. Filter employees whose salary meets or exceeds the cutoff.

    Complexity:
        Time: O(n log n) for groupby and nlargest operations
        Space: O(n) for intermediate columns
    """
    salary_cutoff = (
        employee.drop_duplicates(["salary", "departmentId"])
        .groupby("departmentId")["salary"]
        .nlargest(3)
        .groupby("departmentId")
        .min()
    )
    employee["Department"] = department.set_index("id")["name"][
        employee["departmentId"]
    ].values
    employee["cutoff"] = salary_cutoff[employee["departmentId"]].values
    return employee[employee["salary"] >= employee["cutoff"]].rename(
        columns={"name": "Employee", "salary": "Salary"}
    )[["Department", "Employee", "Salary"]]
