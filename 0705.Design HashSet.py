class MyHashSet:
    """Boolean array-based HashSet for integer keys in known range.

    Intuition:
        With a known key range [0, 10^6], a simple boolean array provides
        O(1) operations for add, remove, and contains.

    Approach:
        1. Allocate a boolean array of size 10^6 + 1.
        2. Add sets the index to True, remove sets to False.
        3. Contains returns the boolean at the index.

    Complexity:
        Time: O(1) for all operations
        Space: O(n) where n is the key range (10^6 + 1)
    """

    def __init__(self) -> None:
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
