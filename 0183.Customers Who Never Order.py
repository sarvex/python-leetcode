import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Pandas Anti-Join Approach

    Intuition:
        Find customers whose id does not appear in the orders table
        using an isin check.

    Approach:
        1. Filter customers whose id is not present in orders customerId.
        2. Select only the name column and rename it to Customers.

    Complexity:
        Time: O(n + m) where n is customers and m is orders
        Space: O(n) for the filtered DataFrame
    """
    non_ordering = customers[~customers["id"].isin(orders["customerId"])]

    return non_ordering[["name"]].rename(columns={"name": "Customers"})
