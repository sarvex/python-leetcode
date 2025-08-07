from typing import List


class SegmentTree:
    """A segment tree implementation for efficient range maximum queries and updates.

    Intuition:
        We need to efficiently find the first basket that can accommodate each fruit
        and update its capacity. A segment tree allows us to do both operations in
        O(log n) time.

    Approach:
        1. Build a segment tree where each node stores the maximum value in its range
        2. For each fruit, find the first basket (leftmost) that can accommodate it
        3. When a basket is used, update its capacity to -1 (indicating it's no longer available)
        4. Count fruits that cannot be placed in any basket

    Complexity:
        - Time: O(n * log m) where n is number of fruits and m is number of baskets
        - Space: O(m) for the segment tree
    """

    def __init__(self, baskets: List[int]) -> None:
        """Initialize the segment tree with basket capacities.

        Args:
            baskets: List of basket capacities
        """
        self.n = len(baskets)
        # Calculate the size needed for the segment tree
        size = 2 << (self.n - 1).bit_length()
        self.tree = [0] * size
        self._build(baskets, 1, 0, self.n - 1)

    def _maintain(self, node_index: int) -> None:
        """Maintain the segment tree property by updating parent nodes.

        Args:
            node_index: Index of the node to maintain
        """
        left_child = node_index * 2
        right_child = node_index * 2 + 1
        self.tree[node_index] = max(self.tree[left_child], self.tree[right_child])

    def _build(self, baskets: List[int], node_index: int, left: int, right: int) -> None:
        """Build the segment tree recursively.

        Args:
            baskets: List of basket capacities
            node_index: Current node index in the segment tree
            left: Left boundary of the current segment
            right: Right boundary of the current segment
        """
        # Base case: leaf node
        if left == right:
            self.tree[node_index] = baskets[left]
            return

        # Recursive case: internal node
        mid = (left + right) // 2
        left_child = node_index * 2
        right_child = node_index * 2 + 1

        self._build(baskets, left_child, left, mid)
        self._build(baskets, right_child, mid + 1, right)
        self._maintain(node_index)

    def find_first_and_update(self, node_index: int, left: int, right: int, min_capacity: int) -> int:
        """Find the first basket that can accommodate a fruit and mark it as used.

        Args:
            node_index: Current node index in the segment tree
            left: Left boundary of the current segment
            right: Right boundary of the current segment
            min_capacity: Minimum capacity required for the fruit

        Returns:
            Index of the first suitable basket, or -1 if none found
        """
        # If no basket in this segment can accommodate the fruit
        if self.tree[node_index] < min_capacity:
            return -1

        # Base case: leaf node
        if left == right:
            # Mark this basket as used by setting its capacity to -1
            self.tree[node_index] = -1
            return left

        # Recursive case: search in children
        mid = (left + right) // 2
        left_child = node_index * 2
        right_child = node_index * 2 + 1

        # First check the left subtree
        basket_index = self.find_first_and_update(left_child, left, mid, min_capacity)

        # If not found in left subtree, check the right subtree
        if basket_index == -1:
            basket_index = self.find_first_and_update(right_child, mid + 1, right, min_capacity)

        # Maintain the segment tree property
        self._maintain(node_index)
        return basket_index


class Solution:
    """Solution for the Fruits Into Baskets III problem.

    Intuition:
        We want to place as many fruits as possible into baskets, with each basket
        holding at most one fruit. We prioritize placing fruits in the first available
        basket (leftmost) that can accommodate each fruit.

    Approach:
        1. Use a segment tree to efficiently find and update basket capacities
        2. For each fruit, find the first basket that can accommodate it
        3. If found, place the fruit and update the basket capacity
        4. If not found, increment the count of unplaced fruits

    Complexity:
        - Time: O(n * log m) where n is number of fruits and m is number of baskets
        - Space: O(m) for the segment tree
    """

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """Calculate the number of fruits that cannot be placed in any basket.

        Args:
            fruits: List of fruit sizes
            baskets: List of basket capacities

        Returns:
            Number of fruits that cannot be placed in any basket
        """
        # Handle edge case: no baskets available
        basket_count = len(baskets)
        if basket_count == 0:
            return len(fruits)

        # Initialize segment tree with basket capacities
        segment_tree = SegmentTree(baskets)

        # Count of fruits that cannot be placed
        unplaced_count = 0

        # Try to place each fruit in the first available basket
        for fruit_size in fruits:
            # Find the first basket that can accommodate this fruit
            basket_index = segment_tree.find_first_and_update(1, 0, basket_count - 1, fruit_size)

            # If no suitable basket found, increment unplaced count
            if basket_index == -1:
                unplaced_count += 1

        return unplaced_count
