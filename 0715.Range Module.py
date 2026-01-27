class Node:
    __slots__ = ["left", "right", "add", "v"]

    def __init__(self) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.add: int = 0
        self.v: bool = False


class SegmentTree:
    __slots__ = ["root"]

    def __init__(self) -> None:
        self.root = Node()

    def modify(
        self,
        left: int,
        right: int,
        value: int,
        lo: int = 1,
        hi: int = int(1e9),
        node: Node | None = None,
    ) -> None:
        if node is None:
            node = self.root
        if lo >= left and hi <= right:
            if value == 1:
                node.add = 1
                node.v = True
            else:
                node.add = -1
                node.v = False
            return
        self.pushdown(node)
        mid = (lo + hi) >> 1
        if left <= mid:
            self.modify(left, right, value, lo, mid, node.left)
        if right > mid:
            self.modify(left, right, value, mid + 1, hi, node.right)
        self.pushup(node)

    def query(
        self,
        left: int,
        right: int,
        lo: int = 1,
        hi: int = int(1e9),
        node: Node | None = None,
    ) -> bool:
        if node is None:
            node = self.root
        if lo >= left and hi <= right:
            return node.v
        self.pushdown(node)
        mid = (lo + hi) >> 1
        result = True
        if left <= mid:
            result = result and self.query(left, right, lo, mid, node.left)
        if right > mid:
            result = result and self.query(left, right, mid + 1, hi, node.right)
        return result

    def pushup(self, node: Node) -> None:
        node.v = bool(node.left and node.left.v and node.right and node.right.v)

    def pushdown(self, node: Node) -> None:
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.add:
            node.left.add = node.right.add = node.add
            node.left.v = node.add == 1
            node.right.v = node.add == 1
            node.add = 0


class RangeModule:
    """Segment tree based range module for tracking intervals.

    Intuition:
        A dynamic segment tree efficiently handles range add/remove/query
        operations on a large coordinate space without materializing all nodes.

    Approach:
        1. Use a lazy propagation segment tree over [1, 10^9].
        2. addRange marks an interval as covered (value 1).
        3. removeRange marks an interval as uncovered (value -1).
        4. queryRange checks if all points in an interval are covered.

    Complexity:
        Time: O(log N) per operation where N is the coordinate range
        Space: O(Q * log N) where Q is the number of operations
    """

    def __init__(self) -> None:
        self.tree = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.tree.modify(left, right - 1, 1)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.modify(left, right - 1, -1)
