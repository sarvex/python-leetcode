class StringIterator:
    """Iterator over a run-length encoded compressed string.

    Intuition:
        Parse the compressed string into character-count pairs upfront,
        then iterate by decrementing counts and advancing the pointer.

    Approach:
        1. Parse the compressed string into a list of [character, count] pairs.
        2. For next(), return current character and decrement its count.
        3. When count reaches zero, advance to the next pair.
        4. For hasNext(), check if the pointer is within bounds with remaining count.

    Complexity:
        Time: O(n) for construction, O(1) per next/hasNext call
        Space: O(n) for storing character-count pairs
    """

    def __init__(self, compressedString: str) -> None:
        self.pairs: list[list] = []
        self.pointer = 0
        length = len(compressedString)
        i = 0
        while i < length:
            char = compressedString[i]
            repeat_count = 0
            i += 1
            while i < length and compressedString[i].isdigit():
                repeat_count = repeat_count * 10 + int(compressedString[i])
                i += 1
            self.pairs.append([char, repeat_count])

    def next(self) -> str:
        if not self.hasNext():
            return " "
        current = self.pairs[self.pointer][0]
        self.pairs[self.pointer][1] -= 1
        if self.pairs[self.pointer][1] == 0:
            self.pointer += 1
        return current

    def hasNext(self) -> bool:
        return self.pointer < len(self.pairs) and self.pairs[self.pointer][1] > 0
