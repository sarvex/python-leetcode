from functools import cache


@cache
def compute_power(x: int) -> int:
    """Compute the power value: steps to reach 1 via Collatz sequence."""
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """Sort integers by their power value and return the k-th element.

        Intuition:
            The power value (steps to reach 1 via the Collatz sequence) can
            be cached to avoid recomputation. Once computed, simply sort by
            power value.

        Approach:
            Use a cached function to compute the power of each integer.
            Sort the range [lo, hi] by power value and return the k-th
            element (1-indexed).

        Complexity:
            Time: O(n log n) where n = hi - lo + 1 for sorting.
            Space: O(n) plus cache space.
        """
        return sorted(range(lo, hi + 1), key=compute_power)[k - 1]
