import random


class RandomizedCollection:
    """Collection supporting insert, delete, and getRandom in O(1) with duplicates.

    Intuition:
        A list provides O(1) random access for getRandom, but deletion
        requires knowing the index. A hash map from values to their index
        sets enables O(1) lookup for swap-and-pop deletion.

    Approach:
        Maintain a list of values and a dictionary mapping each value to
        the set of its indices. To insert, append to the list and record
        the index. To remove, swap the target element with the last element,
        update index sets for both values, then pop the last element.
        getRandom returns a uniformly random element from the list.

    Complexity:
        Time: O(1) average per insert, remove, and getRandom
        Space: O(n) for the value list and index map
    """

    def __init__(self) -> None:
        """Initialize the collection with an index map and value list."""
        self.val_to_indices: dict[int, set[int]] = {}
        self.values: list[int] = []

    def insert(self, val: int) -> bool:
        """Insert a value into the collection.

        Returns True if the collection did not already contain the value.
        """
        index_set = self.val_to_indices.get(val, set())
        index_set.add(len(self.values))
        self.val_to_indices[val] = index_set
        self.values.append(val)
        return len(index_set) == 1

    def remove(self, val: int) -> bool:
        """Remove one instance of a value from the collection.

        Returns True if the collection contained the value.
        """
        if val not in self.val_to_indices:
            return False
        index_set = self.val_to_indices[val]
        remove_idx = list(index_set)[0]
        last_idx = len(self.values) - 1
        self.values[remove_idx] = self.values[last_idx]
        index_set.remove(remove_idx)

        last_index_set = self.val_to_indices[self.values[last_idx]]
        if last_idx in last_index_set:
            last_index_set.remove(last_idx)
        if remove_idx < last_idx:
            last_index_set.add(remove_idx)
        if not index_set:
            self.val_to_indices.pop(val)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        """Return a random element from the collection.

        Each element has equal probability proportional to its count.
        """
        return -1 if len(self.values) == 0 else random.choice(self.values)
