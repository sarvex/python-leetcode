class CombinationIterator:
    """Iterator that generates combinations in lexicographic order.

    Intuition:
        Pre-generate all combinations of the given length using backtracking,
        then iterate through them on demand.

    Approach:
        Use DFS to build all combinations of combinationLength characters from
        the input string. Store them in a list and track the current index for
        iteration.

    Complexity:
        Time: O(C(n, k) * k) for initialization, O(1) for next and hasNext
        Space: O(C(n, k) * k)
    """

    def __init__(self, characters: str, combinationLength: int) -> None:
        def backtrack(start: int) -> None:
            if len(current) == combinationLength:
                self.combinations.append("".join(current))
                return
            if start == total_chars:
                return
            current.append(characters[start])
            backtrack(start + 1)
            current.pop()
            backtrack(start + 1)

        self.combinations: list[str] = []
        total_chars = len(characters)
        current: list[str] = []
        backtrack(0)
        self.index = 0

    def next(self) -> str:
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)
