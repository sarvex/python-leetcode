import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """
    Tagline: Filter active users and compute daily cancellation rate via vectorized operations.

    Intuition: Only trips with non-banned clients and drivers within the target date window count.
    The cancellation rate is the mean of a boolean flag per day.

    Approach:
    - Build the allowed user set where banned == 'No'.
    - Keep trips whose client_id and driver_id are both in the allowed set.
    - Filter trips by request_at between 2013-10-01 and 2013-10-03 inclusive.
    - Derive a boolean 'cancelled' from status containing 'cancelled' (case-insensitive).
    - Group by day and compute the mean, round to 2 decimals, and rename columns.

    Complexity:
    - Time: O(T + U) to filter plus grouping over filtered trips.
    - Space: O(T) for intermediate filtered DataFrame.
    """
    allowed_ids = users.loc[users["banned"] == "No", "users_id"]
    mask_allowed = trips["client_id"].isin(allowed_ids) & trips["driver_id"].isin(allowed_ids)
    mask_date = trips["request_at"].between("2013-10-01", "2013-10-03")
    df = trips.loc[mask_allowed & mask_date].copy()

    df["cancelled"] = df["status"].str.contains("cancelled", case=False, na=False)
    rate = (
        df.groupby("request_at", as_index=False)["cancelled"]
        .mean()
        .round({"cancelled": 2})
        .rename(columns={"request_at": "Day", "cancelled": "Cancellation Rate"})
    )
    return rate
