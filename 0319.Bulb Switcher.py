from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """Mathematical approach counting perfect squares.

        Intuition:
            A bulb ends up on only if it is toggled an odd number of times.
            Bulb i is toggled once for each of its divisors. Only perfect
            squares have an odd number of divisors.

        Approach:
            Return the integer square root of n, which counts the perfect
            squares from 1 to n.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return int(sqrt(n))
