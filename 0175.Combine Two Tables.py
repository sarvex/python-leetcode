import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """Left join person and address tables on personId.

    Intuition:
        Every person should appear in the result regardless of whether they
        have an address, so a left join on personId is appropriate.

    Approach:
        1. Perform a left merge of person and address on personId.
        2. Select only the required columns: firstName, lastName, city, state.

    Complexity:
        Time: O(n + m) where n and m are the sizes of the two tables
        Space: O(n + m)
    """
    return pd.merge(left=person, right=address, how="left", on="personId")[
        ["firstName", "lastName", "city", "state"]
    ]
