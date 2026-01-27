class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries with point updates."""

    __slots__ = ["n", "tree"]

    def __init__(self, n: int) -> None:
        """Initialize tree with n elements."""
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        """Add delta to element at index x."""
        while x <= self.n:
            self.tree[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        """Return prefix sum from index 1 to x."""
        total = 0
        while x > 0:
            total += self.tree[x]
            x -= x & -x
        return total


class NumArray:
    """Mutable array with range sum queries using a Binary Indexed Tree.

    Supports point updates and range sum queries in O(log n) time.
    """

    __slots__ = ["bit"]

    def __init__(self, nums: list[int]) -> None:
        """Initialize by building a BIT from the input array.

        Args:
            nums: The input array of integers.
        """
        self.bit = BinaryIndexedTree(len(nums))
        for i, val in enumerate(nums, 1):
            self.bit.update(i, val)

    def update(self, index: int, val: int) -> None:
        """Update element at index to val.

        Intuition:
            Compute the difference and apply a point update on the BIT.

        Approach:
            Query current value, compute delta, and update the BIT.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        prev = self.sumRange(index, index)
        self.bit.update(index + 1, val - prev)

    def sumRange(self, left: int, right: int) -> int:
        """Return sum of elements between indices left and right inclusive.

        Intuition:
            Prefix sum difference gives range sum.

        Approach:
            Subtract prefix sum at left from prefix sum at right + 1.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        return self.bit.query(right + 1) - self.bit.query(left)
