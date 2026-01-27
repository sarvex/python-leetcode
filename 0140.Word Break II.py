class Trie:
    """Prefix tree for efficient word lookup during segmentation."""

    def __init__(self) -> None:
        """Initialize empty Trie node with 26 children slots."""
        self.children: list[Trie | None] = [None] * 26
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if the word exists in the trie."""
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_end


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """Trie-Based DFS Backtracking Approach

        Intuition:
            Use a Trie for efficient prefix matching and DFS to explore all
            possible word segmentations. Each valid prefix leads to a recursive
            call on the remainder of the string.

        Approach:
            Build a Trie from the dictionary. Use DFS to try all prefixes of the
            remaining string. When a prefix is found in the Trie, recurse on the
            suffix. Collect complete segmentations when the entire string is consumed.

        Complexity:
            Time: O(n * 2^n) in the worst case for generating all segmentations
            Space: O(n * m) for the Trie where m is the number of words
        """

        def dfs(remaining: str) -> list[list[str]]:
            if not remaining:
                return [[]]
            segmentations: list[list[str]] = []
            for i in range(1, len(remaining) + 1):
                if trie.search(remaining[:i]):
                    for suffix_words in dfs(remaining[i:]):
                        segmentations.append([remaining[:i]] + suffix_words)
            return segmentations

        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        all_segmentations = dfs(s)
        return [" ".join(words) for words in all_segmentations]
