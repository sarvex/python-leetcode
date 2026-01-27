class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 26


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        """Trie-based encoding: insert reversed words and sum leaf depths.

        Intuition:
            Words that are suffixes of other words share encoding. Building a
            trie of reversed words groups suffixes together; only leaf nodes
            contribute to the encoding length.

        Approach:
            1. Build a trie by inserting each word in reverse.
            2. DFS the trie to find leaf nodes.
            3. Sum (depth + 1) for each leaf (the +1 accounts for the '#' separator).

        Complexity:
            Time: O(sum of word lengths)
            Space: O(sum of word lengths)
        """
        root = Trie()
        for word in words:
            current = root
            for char in reversed(word):
                idx = ord(char) - ord("a")
                if current.children[idx] is None:
                    current.children[idx] = Trie()
                current = current.children[idx]
        return self._count_leaf_depths(root, 1)

    def _count_leaf_depths(self, node: Trie, depth: int) -> int:
        is_leaf = True
        total = 0
        for i in range(26):
            if node.children[i] is not None:
                is_leaf = False
                total += self._count_leaf_depths(node.children[i], depth + 1)
        if is_leaf:
            total += depth
        return total
