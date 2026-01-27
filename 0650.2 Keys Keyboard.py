from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        """Recursive factorization to find minimum copy-paste operations.

        Intuition:
        The problem reduces to finding the sum of prime factors of n. At each step,
        if n is divisible by i, we can reach n/i first, then copy-paste i times.

        Approach:
        1. Base case: n=1 needs 0 operations.
        2. For each factor i of n, try reaching n/i first then using i operations.
        3. If no factor found, n is prime and needs n operations (copy once, paste n-1 times).
        4. Use memoization to avoid redundant computations.

        Complexity:
        Time: O(n * sqrt(n))
        Space: O(n)
        """

        @cache
        def search(target: int) -> int:
            if target == 1:
                return 0
            factor, result = 2, target
            while factor * factor <= target:
                if target % factor == 0:
                    result = min(result, search(target // factor) + factor)
                factor += 1
            return result

        return search(n)
