from itertools import accumulate


class NumArray:
    """Prefix sum array for immutable range sum queries.

    Uses a prefix sum array to answer range sum queries in O(1) time
    after O(n) preprocessing.
    """

    def __init__(self, nums: list[int]) -> None:
        """Initialize with prefix sum array.

        Args:
            nums: The input array of integers.
        """
        self.prefix = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        """Return sum of elements between indices left and right inclusive.

        Intuition:
            Prefix sums allow O(1) range sum computation.

        Approach:
            Subtract prefix[left] from prefix[right + 1].

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]
