class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        """Sort indices by score to assign rank labels.

        Intuition:
            Sort athletes by score in descending order to determine placement.
            Top 3 get special medal names, rest get numeric ranks.

        Approach:
            Create index array sorted by descending score. Assign medals to
            first three, numeric strings to the rest.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        length = len(score)
        indices = list(range(length))
        indices.sort(key=lambda x: -score[x])
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result: list[str | None] = [None] * length
        for rank in range(length):
            result[indices[rank]] = medals[rank] if rank < 3 else str(rank + 1)
        return result
