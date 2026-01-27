import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    """Pandas Rolling Window Approach

    Intuition:
        Use a rolling window of size 3 to detect three consecutive
        rows with the same number.

    Approach:
        1. Define a lambda to check if all values in a window are the same.
        2. Apply a rolling window of size 3 on the num column.
        3. Filter rows where the rolling check is true and deduplicate.

    Complexity:
        Time: O(n) for the rolling window pass
        Space: O(n) for the is_consecutive column
    """
    all_the_same = lambda lst: lst.nunique() == 1
    logs["is_consecutive"] = (
        logs["num"].rolling(window=3, center=True, min_periods=3).apply(all_the_same)
    )
    return (
        logs.query("is_consecutive == 1.0")[["num"]]
        .drop_duplicates()
        .rename(columns={"num": "ConsecutiveNums"})
    )
