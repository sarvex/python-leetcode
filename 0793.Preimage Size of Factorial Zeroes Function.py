from bisect import bisect_left


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """Binary search on trailing zeroes of factorial.

        Intuition:
            The number of trailing zeroes in n! is determined by the count of
            factor 5. We can binary search for the smallest n with exactly k zeroes.

        Approach:
            1. Define a function to count trailing zeroes of x! by summing x//5^i.
            2. Use binary search to find the first x where trailing_zeroes(x) >= k.
            3. The answer is the difference between searches for k+1 and k.

        Complexity:
            Time: O(log^2(k))
            Space: O(log(k)) for recursion
        """

        def trailing_zeroes(x: int) -> int:
            if x == 0:
                return 0
            return x // 5 + trailing_zeroes(x // 5)

        def first_with_k_zeroes(target: int) -> int:
            return bisect_left(range(5 * target), target, key=trailing_zeroes)

        return first_with_k_zeroes(k + 1) - first_with_k_zeroes(k)
