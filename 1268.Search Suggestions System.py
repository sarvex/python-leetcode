from typing import List, Optional

class Trie:
    """Trie data structure for efficient prefix matching and suggestion retrieval.
    Each node stores up to 3 product indices for suggestions."""
    def __init__(self) -> None:
        self.children: List[Optional[Trie]] = [None] * 26
        self.suggestions: List[int] = []  # Stores up to 3 product indices

    def insert(self, word: str, product_idx: int) -> None:
        """Insert a word into the trie with its product index."""
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            if len(node.suggestions) < 3:
                node.suggestions.append(product_idx)

    def search(self, prefix: str) -> List[List[int]]:
        """Search for prefix and return suggestions for each character.
        Returns a list of suggestion lists for each prefix length."""
        result = [[] for _ in range(len(prefix))]
        node = self

        for i, char in enumerate(prefix):
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                break
            node = node.children[idx]
            result[i] = node.suggestions

        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Trie-based lexicographically sorted product suggestions.

        Intuition:
        Use a trie to efficiently find products with matching prefixes. For each node,
        store up to 3 lexicographically smallest product indices.

        Approach:
        1. Sort products lexicographically
        2. Build a trie with product indices at each node (max 3 per node)
        3. For each prefix of searchWord, retrieve the suggestions

        Complexity:
        Time: O(m*n + k) where m is max product length, n is number of products, k is searchWord length
        Space: O(m*n) for the trie structure
        """
        # Sort products lexicographically
        products.sort()

        # Build trie with product indices
        trie = Trie()
        for i, product in enumerate(products):
            trie.insert(product, i)

        # Get suggestions for each prefix of searchWord
        suggestions_indices = trie.search(searchWord)

        # Convert indices to actual product names
        return [[products[idx] for idx in indices] for indices in suggestions_indices]
