class Node:
    def __init__(self, lo: int, hi: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.lo = lo
        self.hi = hi
        self.mid = (lo + hi) >> 1
        self.value = 0
        self.add = 0


class SegmentTree:
    def __init__(self) -> None:
        self.root = Node(1, int(1e9 + 1))

    def modify(self, lo: int, hi: int, delta: int, node: Node | None = None) -> None:
        if lo > hi:
            return
        if node is None:
            node = self.root
        if node.lo >= lo and node.hi <= hi:
            node.value += delta
            node.add += delta
            return
        self.pushdown(node)
        if lo <= node.mid:
            self.modify(lo, hi, delta, node.left)
        if hi > node.mid:
            self.modify(lo, hi, delta, node.right)
        self.pushup(node)

    def query(self, lo: int, hi: int, node: Node | None = None) -> int:
        if lo > hi:
            return 0
        if node is None:
            node = self.root
        if node.lo >= lo and node.hi <= hi:
            return node.value
        self.pushdown(node)
        result = 0
        if lo <= node.mid:
            result = max(result, self.query(lo, hi, node.left))
        if hi > node.mid:
            result = max(result, self.query(lo, hi, node.right))
        return result

    def pushup(self, node: Node) -> None:
        node.value = max(node.left.value, node.right.value)

    def pushdown(self, node: Node) -> None:
        if node.left is None:
            node.left = Node(node.lo, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.hi)
        if node.add:
            node.left.value += node.add
            node.right.value += node.add
            node.left.add += node.add
            node.right.add += node.add
            node.add = 0


class MyCalendarThree:
    """Segment tree to track maximum overlapping bookings.

    Intuition:
        Each booking adds 1 to an interval. The answer is the maximum value
        across the entire range, which a segment tree with lazy propagation
        can efficiently maintain.

    Approach:
        1. Use a dynamic segment tree over the time range.
        2. On each book call, add +1 to the interval [start+1, end].
        3. Query the entire range for the maximum overlap count.

    Complexity:
        Time: O(log N) per book where N is the coordinate range
        Space: O(Q * log N) where Q is the number of operations
    """

    def __init__(self) -> None:
        self.tree = SegmentTree()

    def book(self, start: int, end: int) -> int:
        self.tree.modify(start + 1, end, 1)
        return self.tree.query(1, int(1e9 + 1))
