import random


class SkiplistNode:
    """Node in a skiplist with value and forward pointers."""

    __slots__ = ["val", "next"]

    def __init__(self, val: int, level: int) -> None:
        self.val = val
        self.next: list[SkiplistNode | None] = [None] * level


class Skiplist:
    """Skiplist implementation supporting search, add, and erase operations.

    Intuition:
        A skiplist provides probabilistic balancing through multiple levels of
        linked lists, giving O(log n) expected time for search, insert, and delete.

    Approach:
        Maintain a head sentinel with max_level forward pointers. Each node has
        a random level. Search, add, and erase traverse from the highest level
        downward, finding the closest predecessor at each level.

    Complexity:
        Time: O(log n) expected per operation
        Space: O(n) expected
    """

    MAX_LEVEL = 32
    PROBABILITY = 0.25

    def __init__(self) -> None:
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        self.level = 0

    def search(self, target: int) -> bool:
        """Return True if target exists in the skiplist."""
        current = self.head
        for i in range(self.level - 1, -1, -1):
            current = self._find_closest(current, i, target)
            if current.next[i] and current.next[i].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        """Insert num into the skiplist."""
        current = self.head
        new_level = self._random_level()
        node = SkiplistNode(num, new_level)
        self.level = max(self.level, new_level)
        for i in range(self.level - 1, -1, -1):
            current = self._find_closest(current, i, num)
            if i < new_level:
                node.next[i] = current.next[i]
                current.next[i] = node

    def erase(self, num: int) -> bool:
        """Remove one occurrence of num. Return True if found."""
        current = self.head
        found = False
        for i in range(self.level - 1, -1, -1):
            current = self._find_closest(current, i, num)
            if current.next[i] and current.next[i].val == num:
                current.next[i] = current.next[i].next[i]
                found = True
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return found

    def _find_closest(
        self, current: SkiplistNode, level: int, target: int
    ) -> SkiplistNode:
        """Find the closest node before target at the given level."""
        while current.next[level] and current.next[level].val < target:
            current = current.next[level]
        return current

    def _random_level(self) -> int:
        """Generate a random level for a new node."""
        level = 1
        while level < self.MAX_LEVEL and random.random() < self.PROBABILITY:
            level += 1
        return level
