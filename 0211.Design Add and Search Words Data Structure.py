class TrieNode:
    """Node in a trie with fixed-size children array for lowercase letters."""

    def __init__(self) -> None:
        self.children: list[TrieNode | None] = [None] * 26
        self.is_end: bool = False


class WordDictionary:
    """Trie-based dictionary supporting exact and wildcard searches.

    Words are stored in a trie. Search supports '.' as a wildcard that
    matches any single character via recursive backtracking.
    """

    def __init__(self) -> None:
        """Initialize the trie with an empty root node."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Add a word to the dictionary.

        Intuition:
            Insert character by character into the trie, creating nodes as
            needed.

        Approach:
            Traverse or create children nodes for each character, then mark
            the final node as a word end.

        Complexity:
            Time: O(m) where m is the word length
            Space: O(m) for new nodes
        """
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Search for a word, where '.' matches any single character.

        Intuition:
            For exact characters, follow the trie path. For '.', branch into
            all non-None children and recursively search the remainder.

        Approach:
            Define a recursive helper that processes characters one at a time.
            On '.', try all 26 children. On a letter, follow the specific child.

        Complexity:
            Time: O(26^d * m) worst case where d is the number of dots
            Space: O(m) recursion depth
        """

        def search_from(remaining: str, node: TrieNode) -> bool:
            for i in range(len(remaining)):
                char = remaining[i]
                index = ord(char) - ord("a")
                if char != "." and node.children[index] is None:
                    return False
                if char == ".":
                    for child in node.children:
                        if child is not None and search_from(remaining[i + 1 :], child):
                            return True
                    return False
                node = node.children[index]
            return node.is_end

        return search_from(word, self.root)
