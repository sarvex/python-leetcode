import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    """Pandas Duplicate Detection Approach

    Intuition:
        Use pandas duplicated method to find emails that appear
        more than once.

    Approach:
        1. Use duplicated on the email column to mark duplicate rows.
        2. Select only the email column from duplicate rows.
        3. Drop duplicates to return each duplicate email once.

    Complexity:
        Time: O(n) for duplicate detection
        Space: O(n) for the result DataFrame
    """
    results = person.loc[person.duplicated(subset=["email"]), ["email"]]

    return results.drop_duplicates()
