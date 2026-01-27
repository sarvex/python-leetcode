from collections import Counter
from functools import reduce
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        """GCD of card frequencies to check valid grouping.

        Intuition:
            Cards can be grouped into equal-sized groups if and only if the
            GCD of all card frequencies is at least 2.

        Approach:
            1. Count the frequency of each card value.
            2. Compute the GCD of all frequencies.
            3. Return whether the GCD is >= 2.

        Complexity:
            Time: O(n log C) where C is the max frequency
            Space: O(n)
        """
        frequency = Counter(deck)
        return reduce(gcd, frequency.values()) >= 2
