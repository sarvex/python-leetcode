import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """Find fraction of players who logged in the day after their first login.

    Intuition:
        Players who return the very next day after their first login represent
        retained users. We compare each player's first login date with their
        other event dates.

    Approach:
        1. Compute the first login date per player using groupby transform.
        2. Filter rows where event_date equals first login + 1 day.
        3. Return the fraction of such players over total unique players.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    activity["first"] = activity.groupby("player_id").event_date.transform(min)
    activity_2nd_day = activity[
        activity["first"] + pd.DateOffset(1) == activity["event_date"]
    ]

    return pd.DataFrame(
        {"fraction": [round(len(activity_2nd_day) / activity.player_id.nunique(), 2)]}
    )
