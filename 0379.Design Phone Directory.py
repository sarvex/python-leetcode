class PhoneDirectory:
    """Phone directory that manages available phone numbers using a set.

    Intuition:
        A set provides O(1) average-case add, remove, and membership check,
        making it ideal for tracking available numbers.

    Approach:
        Initialize a set with all numbers from 0 to maxNumbers-1. get()
        pops an arbitrary element, check() tests membership, and release()
        adds the number back to the set.

    Complexity:
        Time: O(1) amortized per operation
        Space: O(n) where n is maxNumbers
    """

    def __init__(self, maxNumbers: int) -> None:
        """Initialize directory with all numbers from 0 to maxNumbers-1 available."""
        self.available: set[int] = set(range(maxNumbers))

    def get(self) -> int:
        """Provide an available number and mark it as used."""
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number: int) -> bool:
        """Check if a number is available."""
        return number in self.available

    def release(self, number: int) -> None:
        """Release a number and make it available again."""
        self.available.add(number)
