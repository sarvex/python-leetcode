from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        """Return all simplified fractions with denominator <= n.

        Intuition:
            A fraction i/j is simplified if gcd(i, j) == 1.

        Approach:
            Enumerate all numerator-denominator pairs where numerator < denominator
            and filter by gcd being 1.

        Complexity:
            Time: O(n^2 * log(n)) for gcd computations
            Space: O(n^2) for storing results
        """
        return [
            f"{numerator}/{denominator}"
            for numerator in range(1, n)
            for denominator in range(numerator + 1, n + 1)
            if gcd(numerator, denominator) == 1
        ]
