class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        """Maximize candy variety by taking half the total, limited by unique types.

        Intuition:
            The sister can eat at most n/2 candies. To maximize variety, she
            should eat as many distinct types as possible, capped by n/2.

        Approach:
            1. Compute the number of unique candy types.
            2. Return the minimum of unique types and n/2.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        return min(len(candyType) >> 1, len(set(candyType)))
