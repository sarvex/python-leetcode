class Trie:
    """Prefix trie storing word indices for efficient prefix-based lookup."""

    def __init__(self) -> None:
        """Initialize trie node with children and index list."""
        self.children: list[Trie | None] = [None] * 26
        self.indices: list[int] = []

    def insert(self, word: str, index: int) -> None:
        """Insert a word and store its index at every prefix node."""
        node = self
        for char in word:
            child_index = ord(char) - ord("a")
            if node.children[child_index] is None:
                node.children[child_index] = Trie()
            node = node.children[child_index]
            node.indices.append(index)

    def search(self, prefix: str) -> list[int]:
        """Return indices of all words matching the given prefix."""
        node = self
        for char in prefix:
            child_index = ord(char) - ord("a")
            if node.children[child_index] is None:
                return []
            node = node.children[child_index]
        return node.indices


class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        """Backtracking with trie-based prefix search to build word squares.

        Intuition:
            A word square requires that the k-th column of chosen words forms
            the k-th row. At each step, the prefix for the next word is determined
            by the columns of already-chosen words.

        Approach:
            1. Build a trie indexing all words by their prefixes.
            2. For each word, start a DFS trying to build a complete square.
            3. At each depth, compute the required prefix from existing columns
               and find all matching words via trie lookup.
            4. Collect all valid squares.

        Complexity:
            Time: O(n * 26^L) in the worst case where L is word length.
            Space: O(n * L) for the trie storage.
        """

        def dfs(current_square: list[str]) -> None:
            if len(current_square) == len(words[0]):
                result.append(current_square[:])
                return
            depth = len(current_square)
            prefix = [word[depth] for word in current_square]
            matching_indices = trie.search("".join(prefix))
            for idx in matching_indices:
                current_square.append(words[idx])
                dfs(current_square)
                current_square.pop()

        trie = Trie()
        result: list[list[str]] = []
        for i, word in enumerate(words):
            trie.insert(word, i)
        for word in words:
            dfs([word])
        return result
