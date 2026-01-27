class ZigzagIterator:
    """Iterator that alternates elements from two lists in zigzag order.

    Intuition:
        Round-robin through the input lists, pulling one element at a time
        from each list in turn, skipping exhausted lists.

    Approach:
        Maintain an array of index pointers (one per list) and a cursor
        indicating which list to pull from next. On next(), return the
        element at the current cursor's index and advance both the index
        and cursor. On hasNext(), cycle the cursor forward past exhausted
        lists to find one with remaining elements.

    Complexity:
        Time: O(1) per next, O(k) per hasNext where k is the number of lists
        Space: O(k) for index tracking
    """

    def __init__(self, v1: list[int], v2: list[int]) -> None:
        """Initialize with two integer lists to zigzag through."""
        self.current = 0
        self.size = 2
        self.indexes = [0] * self.size
        self.vectors = [v1, v2]

    def next(self) -> int:
        """Return the next element in zigzag order."""
        vector = self.vectors[self.current]
        index = self.indexes[self.current]
        result = vector[index]
        self.indexes[self.current] = index + 1
        self.current = (self.current + 1) % self.size
        return result

    def hasNext(self) -> bool:
        """Return True if there are remaining elements in either list."""
        start = self.current
        while self.indexes[self.current] == len(self.vectors[self.current]):
            self.current = (self.current + 1) % self.size
            if self.current == start:
                return False
        return True
