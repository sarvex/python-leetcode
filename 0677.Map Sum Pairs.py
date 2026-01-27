from collections import defaultdict


class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 26
        self.val: int = 0

    def insert(self, word: str, delta: int) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.val += delta

    def search(self, prefix: str) -> int:
        node = self
        for char in prefix:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                return 0
            node = node.children[idx]
        return node.val


class MapSum:
    """Trie with prefix sum tracking using delta updates.

    Intuition:
        To efficiently compute the sum of values for all keys with a given
        prefix, we can store cumulative values in trie nodes and apply deltas
        on insert to handle key updates.

    Approach:
        1. Maintain a trie where each node stores the sum of all values passing
           through it.
        2. Track previously inserted values in a dictionary.
        3. On insert, compute the delta (new value - old value) and propagate
           it through the trie path.
        4. For sum queries, traverse the trie to the prefix end node.

    Complexity:
        Time: O(L) per insert and sum operation where L is key/prefix length
        Space: O(N * L) for the trie
    """

    def __init__(self) -> None:
        self.key_values: dict[str, int] = defaultdict(int)
        self.tree = Trie()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_values[key]
        self.key_values[key] = val
        self.tree.insert(key, delta)

    def sum(self, prefix: str) -> int:
        return self.tree.search(prefix)
