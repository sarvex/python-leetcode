from collections import Counter, OrderedDict


class FirstUnique:
    """Track first unique number in a stream using ordered dict.

    Intuition:
        Maintain an ordered collection of unique numbers and a frequency counter
        to efficiently find and update the first unique element.

    Approach:
        Use a Counter for frequencies and an OrderedDict for unique values.
        On add, increment the count; if count becomes 1 add to ordered dict,
        otherwise remove from ordered dict if present.

    Complexity:
        Time: O(1) amortized for showFirstUnique and add
        Space: O(n) for storing counts and unique values
    """

    def __init__(self, nums: list[int]):
        self.count = Counter(nums)
        self.unique = OrderedDict({val: 1 for val in nums if self.count[val] == 1})

    def showFirstUnique(self) -> int:
        return -1 if not self.unique else next(iter(self.unique))

    def add(self, value: int) -> None:
        self.count[value] += 1
        if self.count[value] == 1:
            self.unique[value] = 1
        elif value in self.unique:
            self.unique.pop(value)
