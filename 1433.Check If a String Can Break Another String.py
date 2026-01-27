class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """Check if one sorted string dominates the other character-wise.

        Intuition:
            If one string can break another, then when both are sorted, one
            must be >= the other at every position.

        Approach:
            Sort both strings and check if either sorted string is pointwise
            greater than or equal to the other.

        Complexity:
            Time: O(n log n) for sorting
            Space: O(n) for sorted copies
        """
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        return all(a >= b for a, b in zip(sorted_s1, sorted_s2)) or all(
            a <= b for a, b in zip(sorted_s1, sorted_s2)
        )
