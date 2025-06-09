from random import choice

class RandomizedSet:
    """
    O(1) Operations: A data structure that supports insert, remove, and getRandom operations in O(1) time.

    Intuition:
    Use a list for O(1) random access and a dictionary for O(1) lookups.
    The key insight is maintaining the mapping between values and their indices in the list.

    Approach:
    1. Use a dictionary to store value -> index mapping for O(1) lookups
    2. Use a list to store values for O(1) random access
    3. For removal, swap the element to remove with the last element, then pop

    Complexity:
    Time: O(1) for all operations (insert, remove, getRandom)
    Space: O(n) where n is the number of elements in the set
    """
    def __init__(self) -> None:
        self.indices = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        idx = self.indices[val]
        last_val = self.values[-1]

        self.values[idx] = last_val
        self.indices[last_val] = idx

        self.values.pop()
        self.indices.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
