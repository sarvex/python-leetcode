class Vector2D:
    """Iterator that flattens a 2D vector into a 1D sequence.

    Intuition:
        Traverse a 2D structure sequentially by maintaining row and column
        indices, skipping over empty inner lists.

    Approach:
        Use an outer index and inner index to track the current position.
        A forward helper advances past empty inner lists before each access.
        next() returns the current element and increments the inner index,
        while hasNext() checks whether a valid position exists.

    Complexity:
        Time: O(1) amortized per next/hasNext call
        Space: O(1) extra beyond the input reference
    """

    def __init__(self, vec: list[list[int]]) -> None:
        """Initialize with a 2D vector."""
        self.outer = 0
        self.inner = 0
        self.vec = vec

    def next(self) -> int:
        """Return the next element in the flattened iteration."""
        self.forward()
        value = self.vec[self.outer][self.inner]
        self.inner += 1
        return value

    def hasNext(self) -> bool:
        """Check if there are remaining elements."""
        self.forward()
        return self.outer < len(self.vec)

    def forward(self) -> None:
        """Advance past empty inner lists to the next valid element."""
        while self.outer < len(self.vec) and self.inner >= len(self.vec[self.outer]):
            self.outer += 1
            self.inner = 0
