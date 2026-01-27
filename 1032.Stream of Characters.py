class Trie:
    """Trie that stores words in reverse for suffix matching."""

    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for char in reversed(word):
            index = ord(char) - ord("a")
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True

    def search(self, characters: list[str]) -> bool:
        node = self
        for char in reversed(characters):
            index = ord(char) - ord("a")
            if node.children[index] is None:
                return False
            node = node.children[index]
            if node.is_end:
                return True
        return False


class StreamChecker:
    """Stream of Characters using reverse-order Trie.

    Intuition:
        Instead of checking all prefixes, store words reversed in a trie and
        check the stream buffer from most recent character backwards.

    Approach:
        Insert all words reversed into a trie. On each query, append the
        character to a buffer and search the trie using the buffer's suffix
        (up to the max word length).

    Complexity:
        Time: O(L) per query where L is max word length; O(sum of word lengths) for init
        Space: O(sum of word lengths) for trie + O(L) for buffer
    """

    def __init__(self, words: list[str]) -> None:
        self.trie = Trie()
        self.stream: list[str] = []
        self.max_length = 201
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.trie.search(self.stream[-self.max_length :])
