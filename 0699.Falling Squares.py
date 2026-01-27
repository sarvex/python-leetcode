class SegmentNode:
    def __init__(self, left_bound: int, right_bound: int) -> None:
        self.left: SegmentNode | None = None
        self.right: SegmentNode | None = None
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.mid = (left_bound + right_bound) >> 1
        self.value = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self) -> None:
        self.root = SegmentNode(1, int(1e9))

    def modify(
        self, left: int, right: int, value: int, node: SegmentNode | None = None
    ) -> None:
        if left > right:
            return
        if node is None:
            node = self.root
        if node.left_bound >= left and node.right_bound <= right:
            node.value = value
            node.lazy = value
            return
        self._pushdown(node)
        if left <= node.mid:
            self.modify(left, right, value, node.left)
        if right > node.mid:
            self.modify(left, right, value, node.right)
        self._pushup(node)

    def query(self, left: int, right: int, node: SegmentNode | None = None) -> int:
        if left > right:
            return 0
        if node is None:
            node = self.root
        if node.left_bound >= left and node.right_bound <= right:
            return node.value
        self._pushdown(node)
        result = 0
        if left <= node.mid:
            result = max(result, self.query(left, right, node.left))
        if right > node.mid:
            result = max(result, self.query(left, right, node.right))
        return result

    def _pushup(self, node: SegmentNode) -> None:
        node.value = max(node.left.value, node.right.value)

    def _pushdown(self, node: SegmentNode) -> None:
        if node.left is None:
            node.left = SegmentNode(node.left_bound, node.mid)
        if node.right is None:
            node.right = SegmentNode(node.mid + 1, node.right_bound)
        if node.lazy:
            node.left.value = node.lazy
            node.right.value = node.lazy
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
            node.lazy = 0


class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        """Lazy segment tree to track maximum height after each falling square.

        Intuition:
            Each square lands on the highest point in its range and adds its
            height. A segment tree with lazy propagation efficiently queries
            max height over a range and updates ranges.

        Approach:
            1. For each square, query the max height in its landing range.
            2. New height = queried max + square side length.
            3. Update the range with the new height.
            4. Track the running maximum across all squares.

        Complexity:
            Time: O(n log C) where C is coordinate range and n is number of squares
            Space: O(n log C) for the dynamically allocated segment tree nodes
        """
        result: list[int] = []
        max_height = 0
        tree = SegmentTree()
        for left, width in positions:
            right = left + width - 1
            height = tree.query(left, right) + width
            max_height = max(max_height, height)
            result.append(max_height)
            tree.modify(left, right, height)
        return result
