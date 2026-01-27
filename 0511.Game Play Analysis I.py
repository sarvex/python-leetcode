import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """Find each player's first login date using groupby aggregation.

    Intuition:
        The first login is simply the minimum event_date per player.

    Approach:
        Group by player_id and aggregate event_date with min function.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    return (
        activity.groupby("player_id")
        .agg(first_login=("event_date", "min"))
        .reset_index()
    )
