from bisect import bisect_left
from math import lcm


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """Binary search using inclusion-exclusion to count magical numbers.

        Intuition:
            A magical number is divisible by a or b. Using inclusion-exclusion,
            count how many magical numbers exist up to x, then binary search
            for the nth one.

        Approach:
            1. Compute LCM of a and b for inclusion-exclusion.
            2. Binary search over the range [0, (a+b)*n] for the smallest x
               where the count of magical numbers up to x equals n.
            3. The count function is x//a + x//b - x//lcm(a,b).

        Complexity:
            Time: O(log((a + b) * n))
            Space: O(1)
        """
        modulo = 10**9 + 7
        common_multiple = lcm(a, b)
        upper_bound = (a + b) * n
        return (
            bisect_left(
                range(upper_bound),
                x=n,
                key=lambda x: x // a + x // b - x // common_multiple,
            )
            % modulo
        )
