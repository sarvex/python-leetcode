from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        One-pass solution with list comprehension

        Intuition:
        If a kid can have the greatest number of candies, their current candies plus
        the extra candies must be greater than or equal to the current maximum.

        Approach:
        1. Find the maximum number of candies among all kids
        2. For each kid, check if their candies plus extra candies is >= maximum
        3. Return the result as a list of booleans

        Complexity:
        Time: O(n) where n is the number of kids (we need one pass to find max, one to create result)
        Space: O(n) for the output list
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
