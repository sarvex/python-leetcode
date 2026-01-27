from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        """Count pairs of dominoes that are equivalent after rotation.

        Intuition:
            Two dominoes are equivalent if one can be rotated to match the
            other. Normalize each domino by sorting its values.

        Approach:
            Encode each domino as a canonical integer (smaller digit * 10 +
            larger digit). Count occurrences and sum pairs using the running
            count before incrementing.

        Complexity:
            Time: O(n) where n is the number of dominoes
            Space: O(1) since there are at most 45 distinct domino values
        """
        count: Counter[int] = Counter()
        result = 0
        for top, bottom in dominoes:
            key = top * 10 + bottom if top < bottom else bottom * 10 + top
            result += count[key]
            count[key] += 1
        return result
