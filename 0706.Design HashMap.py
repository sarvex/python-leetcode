class MyHashMap:
    """Array-based HashMap for integer keys in known range.

    Intuition:
        With a known key range [0, 10^6], a direct-address table using an
        array provides O(1) operations. Use -1 as the sentinel for missing keys.

    Approach:
        1. Allocate an integer array of size 10^6 + 1 initialized to -1.
        2. Put stores the value at the key index.
        3. Get returns the value at the key index (-1 if absent).
        4. Remove resets the key index to -1.

    Complexity:
        Time: O(1) for all operations
        Space: O(n) where n is the key range (10^6 + 1)
    """

    def __init__(self) -> None:
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1
