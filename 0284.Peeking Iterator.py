class PeekingIterator:
    """Iterator wrapper that supports peeking at the next element without consuming it.

    Intuition:
        Cache one element ahead so that peek can return it without advancing
        the underlying iterator, and next can return the cached value when
        available.

    Approach:
        Maintain a flag indicating whether an element has been peeked and a
        variable storing the peeked value. On peek(), if not already peeked,
        advance the underlying iterator and cache the result. On next(),
        return the cached value if peeked, otherwise delegate to the
        underlying iterator. hasNext() returns True if either a value is
        cached or the underlying iterator has more elements.

    Complexity:
        Time: O(1) per peek, next, and hasNext
        Space: O(1) extra for the cached element
    """

    def __init__(self, iterator: "Iterator") -> None:
        """Initialize with an underlying iterator."""
        self.iterator = iterator
        self.has_peeked = False
        self.peeked_element: int | None = None

    def peek(self) -> int:
        """Return the next element without advancing the iterator."""
        if not self.has_peeked:
            self.peeked_element = self.iterator.next()
            self.has_peeked = True
        return self.peeked_element

    def next(self) -> int:
        """Return the next element and advance the iterator."""
        if not self.has_peeked:
            return self.iterator.next()
        result = self.peeked_element
        self.has_peeked = False
        self.peeked_element = None
        return result

    def hasNext(self) -> bool:
        """Return True if the iterator has more elements."""
        return self.has_peeked or self.iterator.hasNext()
