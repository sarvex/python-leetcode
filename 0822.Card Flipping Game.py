from itertools import chain


class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        """Find minimum value not on both sides of any card.

        Intuition:
            A number that appears on both front and back of the same card can
            never be hidden. Among all other numbers, find the minimum.

        Approach:
            1. Collect all numbers where front == back (these are always visible).
            2. Find the minimum number from all fronts and backs not in that set.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        same_on_both = {front for front, back in zip(fronts, backs) if front == back}
        return min(
            (x for x in chain(fronts, backs) if x not in same_on_both), default=0
        )
