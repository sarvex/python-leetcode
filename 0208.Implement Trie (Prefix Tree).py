class Trie:
    """Array-based Trie implementation for lowercase English letters.

    Intuition:
        Use an array of size 26 for each node to represent possible child nodes,
        where each index corresponds to a lowercase letter (a-z).

    Approach:
        - Each Trie node contains an array of 26 pointers to child nodes
        - Use a boolean flag to mark the end of a word
        - For operations, traverse the trie character by character
        - For search and prefix matching, use a helper method to find nodes

    Complexity:
        Time: O(m) for all operations, where m is the key length
        Space: O(n*m) where n is number of keys and m is average key length
    """

    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix: str) -> 'Trie | None':
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
