from functools import reduce
from math import gcd


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        """Check if subset sums can produce 1 using Bezout's identity.

        Intuition:
            By Bezout's identity, a subset of integers can produce 1 as a linear
            combination if and only if their GCD is 1. This transforms the problem
            into checking whether the GCD of all elements equals 1.

        Approach:
            Compute the GCD of all elements in the array using reduce. If the
            result is 1, the array is a good array.

        Complexity:
            Time: O(n log(max_val)) — GCD computation for each element
            Space: O(1) — constant extra space
        """
        return reduce(gcd, nums) == 1
