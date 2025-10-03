import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    """Return rows that belong to any 3-length window with all people >= 100.

    Tagline: Use a rolling(3).min() trick to flag windows with all values >= 100.

    Intuition:
    If the minimum over a rolling window of size 3 is >= 100, that window qualifies.
    A row belongs to a qualifying window if it is in the window itself or in the next
    one or two positions, hence checking the current rolling min and its forward shifts.

    Approach:
    - Sort by id to respect row order (matching SQL ORDER BY behavior).
    - Compute m = people.rolling(3).min().
    - Keep rows where m >= 100 or m.shift(-1) >= 100 or m.shift(-2) >= 100.
    - Return id, visit_date, people sorted by id.

    Complexity:
    - Time: O(n log n) for sorting; O(n) for rolling and filtering
    - Space: O(n)
    """
    df = stadium.sort_values("id", kind="mergesort").copy()
    m = df["people"].rolling(3).min()
    keep = (m >= 100) | (m.shift(-1) >= 100) | (m.shift(-2) >= 100)
    result = df.loc[keep, ["id", "visit_date", "people"]]
    return result.sort_values("id").reset_index(drop=True)
