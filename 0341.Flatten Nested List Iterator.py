class NestedIterator:
    """Iterator that flattens a nested list of integers.

    Intuition:
        Pre-flatten the entire nested structure so that iteration becomes
        a simple sequential scan over a flat list.

    Approach:
        Use DFS to recursively traverse the nested list. For each element,
        if it is an integer, append it to the flat list; otherwise recurse
        into its nested list. next() and hasNext() then operate on the
        pre-built flat list using an index pointer.

    Complexity:
        Time: O(n) for initialization, O(1) per next and hasNext
        Space: O(n) for the flattened list
    """

    def __init__(self, nestedList: list["NestedInteger"]) -> None:
        """Flatten the nested list into a simple integer list."""

        def dfs(items: list["NestedInteger"]) -> None:
            for item in items:
                if item.isInteger():
                    self.nums.append(item.getInteger())
                else:
                    dfs(item.getList())

        self.nums: list[int] = []
        self.index = -1
        dfs(nestedList)

    def next(self) -> int:
        """Return the next integer in the flattened sequence."""
        self.index += 1
        return self.nums[self.index]

    def hasNext(self) -> bool:
        """Check if there are remaining integers."""
        return self.index + 1 < len(self.nums)
