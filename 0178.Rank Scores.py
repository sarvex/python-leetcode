import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """Pandas Dense Rank Approach

    Intuition:
        Use dense ranking to assign consecutive ranks with no gaps
        to scores sorted in descending order.

    Approach:
        1. Apply dense rank method on the score column in descending order.
        2. Drop the id column as it is not needed in the result.
        3. Sort the DataFrame by score in descending order.

    Complexity:
        Time: O(n log n) for ranking and sorting
        Space: O(n) for the rank column
    """
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)

    result_df = scores.drop("id", axis=1).sort_values(by="score", ascending=False)

    return result_df
