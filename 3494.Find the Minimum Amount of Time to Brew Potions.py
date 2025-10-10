from typing import List
from itertools import accumulate, pairwise


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        """
        Calculate the minimum time to brew all potions with optimal parallel processing.

        Intuition:
        - We can brew multiple potions in parallel, but each potion requires a minimum time based on its skill level.
        - The total time is the sum of the maximum skill level in each parallel batch, multiplied by the corresponding mana cost.

        Approach:
        1. Calculate the base time if we brew all potions in parallel at the last mana cost.
        2. For each pair of consecutive mana costs (m1, m2), calculate the optimal split point where:
           - Potions before the split are brewed at m1
           - Potions at and after the split are brewed at m2
        3. The optimal split is found by maximizing (prefix_sum * m1 - offset_sum * m2)

        Complexity:
        - Time: O(n^2) in the worst case, but optimized with numpy operations
        - Space: O(n) for storing prefix sums and offsets
        """
        if not skill or not mana:
            return 0

        # Calculate base case: all potions brewed at the last mana cost
        total_time = sum(skill) * mana[-1]

        # Calculate prefix sums for efficient range sum queries
        prefix_sums = list(accumulate(skill))

        # Calculate offsets (sum of all elements before current index)
        offsets = [0] * len(skill)
        for i in range(1, len(skill)):
            offsets[i] = prefix_sums[i - 1]

        # For each pair of consecutive mana costs
        for m1, m2 in pairwise(mana):
            max_diff = 0
            # Find the maximum (prefix_sum[i] * m1 - offsets[i] * m2)
            for i in range(len(skill)):
                current_diff = prefix_sums[i] * m1 - offsets[i] * m2
                if current_diff > max_diff:
                    max_diff = current_diff

            total_time += max_diff

        return total_time
