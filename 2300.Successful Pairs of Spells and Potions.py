from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """Binary search approach to find successful spell-potion pairs.

        Intuition:
            For each spell, we need to count potions that create a product ≥ success.
            If we sort potions, we can use binary search to efficiently find this count.

        Approach:
            1. Sort the potions array
            2. For each spell, calculate the minimum potion strength needed (success/spell)
            3. Use binary search to find the index of the first potion that meets the requirement
            4. Calculate how many potions are valid (total - index)

        Complexity:
            Time: O(n log m + m log m) where n is len(spells) and m is len(potions)
            Space: O(n) for the result array
        """
        potions.sort()
        m = len(potions)

        def count_successful_pairs(spell: int) -> int:
            # Find minimum potion strength needed using ceiling division
            min_strength = -(-success // spell)
            # Find index of first potion that works
            idx = bisect_left(potions, min_strength)
            # Return count of valid potions
            return m - idx

        return [count_successful_pairs(spell) for spell in spells]
