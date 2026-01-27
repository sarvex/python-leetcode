from math import isqrt


class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        """Find two integers whose product is num+1 or num+2 with minimum difference.

        Intuition:
            The closest pair of factors of a number are found near its square
            root. Check both num+1 and num+2 to find the pair with the
            smallest absolute difference.

        Approach:
            For each candidate (num+1 and num+2), iterate downward from the
            square root to find the largest divisor, then return the pair
            with the smaller difference between factors.

        Complexity:
            Time: O(sqrt(num))
            Space: O(1)
        """

        def find_closest_pair(x: int) -> list[int]:
            for divisor in range(isqrt(x), 0, -1):
                if x % divisor == 0:
                    return [divisor, x // divisor]
            return [1, x]

        pair_a = find_closest_pair(num + 1)
        pair_b = find_closest_pair(num + 2)
        return (
            pair_a
            if abs(pair_a[0] - pair_a[1]) < abs(pair_b[0] - pair_b[1])
            else pair_b
        )
