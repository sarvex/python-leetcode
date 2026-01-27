from bisect import bisect_left
from collections import defaultdict


class Node:
    """Segment tree node storing majority candidate and count."""

    __slots__ = ("left", "right", "candidate", "count")

    def __init__(self) -> None:
        self.left = self.right = 0
        self.candidate = self.count = 0


class SegmentTree:
    """Segment tree for Boyer-Moore majority vote queries."""

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums
        n = len(nums)
        self.nodes = [Node() for _ in range(n << 2)]
        self._build(1, 1, n)

    def _build(self, node_idx: int, left: int, right: int) -> None:
        self.nodes[node_idx].left, self.nodes[node_idx].right = left, right
        if left == right:
            self.nodes[node_idx].candidate = self.nums[left - 1]
            self.nodes[node_idx].count = 1
            return
        mid = (left + right) >> 1
        self._build(node_idx << 1, left, mid)
        self._build(node_idx << 1 | 1, mid + 1, right)
        self._pushup(node_idx)

    def query(self, node_idx: int, left: int, right: int) -> tuple[int, int]:
        """Query the majority candidate and count in range [left, right]."""
        if self.nodes[node_idx].left >= left and self.nodes[node_idx].right <= right:
            return self.nodes[node_idx].candidate, self.nodes[node_idx].count
        mid = (self.nodes[node_idx].left + self.nodes[node_idx].right) >> 1
        if right <= mid:
            return self.query(node_idx << 1, left, right)
        if left > mid:
            return self.query(node_idx << 1 | 1, left, right)
        cand1, cnt1 = self.query(node_idx << 1, left, right)
        cand2, cnt2 = self.query(node_idx << 1 | 1, left, right)
        if cand1 == cand2:
            return cand1, cnt1 + cnt2
        if cnt1 >= cnt2:
            return cand1, cnt1 - cnt2
        return cand2, cnt2 - cnt1

    def _pushup(self, node_idx: int) -> None:
        left_child = self.nodes[node_idx << 1]
        right_child = self.nodes[node_idx << 1 | 1]
        if left_child.candidate == right_child.candidate:
            self.nodes[node_idx].candidate = left_child.candidate
            self.nodes[node_idx].count = left_child.count + right_child.count
        elif left_child.count >= right_child.count:
            self.nodes[node_idx].candidate = left_child.candidate
            self.nodes[node_idx].count = left_child.count - right_child.count
        else:
            self.nodes[node_idx].candidate = right_child.candidate
            self.nodes[node_idx].count = right_child.count - left_child.count


class MajorityChecker:
    """Online majority element checker using segment tree and binary search.

    Intuition:
        Use Boyer-Moore voting in a segment tree to find the majority candidate,
        then verify using binary search on precomputed index lists.

    Approach:
        Build a segment tree with Boyer-Moore majority vote at each node. For
        each query, get the candidate from the segment tree, then verify its
        actual count in the range using binary search on stored indices.

    Complexity:
        Time: O(n) build, O(log^2 n) per query
        Space: O(n)
    """

    def __init__(self, arr: list[int]) -> None:
        self.tree = SegmentTree(arr)
        self.indices: dict[int, list[int]] = defaultdict(list)
        for i, value in enumerate(arr):
            self.indices[value].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        """Return majority element if it meets threshold, otherwise -1."""
        candidate, _ = self.tree.query(1, left + 1, right + 1)
        lo = bisect_left(self.indices[candidate], left)
        hi = bisect_left(self.indices[candidate], right + 1)
        return candidate if hi - lo >= threshold else -1
