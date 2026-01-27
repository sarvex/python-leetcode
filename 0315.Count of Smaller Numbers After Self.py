class BinaryIndexedTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries with point updates."""

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


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        """BIT-based approach counting smaller elements to the right.

        Intuition:
            Process elements from right to left. For each element, query how
            many previously inserted elements are smaller using a BIT.

        Approach:
            1. Coordinate compress the values to a range [1, m].
            2. Traverse nums from right to left.
            3. For each value, query the BIT for the count of elements smaller
               than it, then insert the current value into the BIT.
            4. Reverse the result to match original order.

        Complexity:
            Time: O(n log n) where n is the length of nums
            Space: O(n) for the BIT and coordinate mapping
        """
        sorted_unique = sorted(set(nums))
        rank_map = {val: i for i, val in enumerate(sorted_unique, 1)}
        tree = BinaryIndexedTree(len(rank_map))
        result = []
        for val in nums[::-1]:
            rank = rank_map[val]
            tree.update(rank, 1)
            result.append(tree.query(rank - 1))
        return result[::-1]
