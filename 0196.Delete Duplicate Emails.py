import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """Pandas In-Place Deduplication Approach

    Intuition:
        Sort by id to keep the smallest id for each email, then
        drop duplicates in place.

    Approach:
        1. Sort the DataFrame by id in ascending order.
        2. Drop duplicate rows based on email, keeping the first occurrence.
        3. Modify the DataFrame in place.

    Complexity:
        Time: O(n log n) for sorting
        Space: O(n) for the sorted intermediate
    """
    person.sort_values(by="id", ascending=True, inplace=True)
    person.drop_duplicates(subset="email", keep="first", inplace=True)
