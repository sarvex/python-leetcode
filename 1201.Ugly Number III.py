from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """Find the nth ugly number divisible by a, b, or c using binary search.

        Intuition:
            Use inclusion-exclusion to count numbers divisible by a, b, or c
            up to a given value, then binary search for the smallest value
            with exactly n such numbers.

        Approach:
            Precompute LCMs of all pairs and the triple. Binary search on the
            answer, using inclusion-exclusion to count how many numbers up to
            mid are divisible by a, b, or c.

        Complexity:
            Time: O(log(2 * 10^9))
            Space: O(1)
        """
        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        lcm_abc = lcm(a, b, c)
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) >> 1
            count = (
                mid // a
                + mid // b
                + mid // c
                - mid // lcm_ab
                - mid // lcm_bc
                - mid // lcm_ac
                + mid // lcm_abc
            )
            if count >= n:
                right = mid
            else:
                left = mid + 1
        return left
