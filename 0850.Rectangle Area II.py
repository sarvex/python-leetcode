class Node:
    def __init__(self) -> None:
        self.left = self.right = 0
        self.count = self.length = 0


class SegmentTree:
    def __init__(self, coords: list[int]) -> None:
        num_intervals = len(coords) - 1
        self.coords = coords
        self.tree = [Node() for _ in range(num_intervals << 2)]
        self._build(1, 0, num_intervals - 1)

    def _build(self, node_idx: int, left: int, right: int) -> None:
        self.tree[node_idx].left, self.tree[node_idx].right = left, right
        if left != right:
            mid = (left + right) >> 1
            self._build(node_idx << 1, left, mid)
            self._build(node_idx << 1 | 1, mid + 1, right)

    def modify(self, node_idx: int, left: int, right: int, delta: int) -> None:
        if self.tree[node_idx].left >= left and self.tree[node_idx].right <= right:
            self.tree[node_idx].count += delta
        else:
            mid = (self.tree[node_idx].left + self.tree[node_idx].right) >> 1
            if left <= mid:
                self.modify(node_idx << 1, left, right, delta)
            if right > mid:
                self.modify(node_idx << 1 | 1, left, right, delta)
        self._push_up(node_idx)

    def _push_up(self, node_idx: int) -> None:
        if self.tree[node_idx].count:
            self.tree[node_idx].length = (
                self.coords[self.tree[node_idx].right + 1]
                - self.coords[self.tree[node_idx].left]
            )
        elif self.tree[node_idx].left == self.tree[node_idx].right:
            self.tree[node_idx].length = 0
        else:
            self.tree[node_idx].length = (
                self.tree[node_idx << 1].length + self.tree[node_idx << 1 | 1].length
            )

    @property
    def total_length(self) -> int:
        return self.tree[1].length


class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        """Sweep line with segment tree for rectangle union area.

        Intuition:
            Use a vertical sweep line moving left to right. At each x-coordinate
            event, update the segment tree with the active y-intervals and
            accumulate the area.

        Approach:
            1. Create events for left and right edges of each rectangle.
            2. Coordinate-compress y-values and build a segment tree.
            3. Process events in x-order, updating active intervals and
               accumulating area as width * active_length.

        Complexity:
            Time: O(n^2 log n) where n = number of rectangles
            Space: O(n)
        """
        events: list[tuple[int, int, int, int]] = []
        y_coords_set: set[int] = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))
            y_coords_set.update([y1, y2])

        events.sort()
        y_coords = sorted(y_coords_set)
        seg_tree = SegmentTree(y_coords)
        coord_to_index = {value: i for i, value in enumerate(y_coords)}
        total_area = 0
        for i, (x_pos, y1, y2, delta) in enumerate(events):
            if i:
                total_area += seg_tree.total_length * (x_pos - events[i - 1][0])
            seg_tree.modify(1, coord_to_index[y1], coord_to_index[y2] - 1, delta)
        total_area %= 10**9 + 7
        return total_area
