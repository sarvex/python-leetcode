class Trie:
    __slots__ = ["children", "is_end"]

    def __init__(self) -> None:
        self.children: dict[str, Trie] = {}
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: Trie, diff: int) -> bool:
            if index == len(word):
                return diff == 1 and node.is_end
            if word[index] in node.children and dfs(
                index + 1, node.children[word[index]], diff
            ):
                return True
            return diff == 0 and any(
                dfs(index + 1, node.children[char], 1)
                for char in node.children
                if char != word[index]
            )

        return dfs(0, self, 0)


class MagicDictionary:
    """Trie-based dictionary with single-character difference search.

    Intuition:
        A trie allows efficient prefix-based traversal. By allowing exactly one
        character substitution during search, we can check if any word in the
        dictionary differs by exactly one character.

    Approach:
        1. Build a trie from the dictionary words.
        2. For search, use DFS on the trie tracking how many characters differ.
        3. Allow branching into non-matching children only when no difference
           has been used yet. Return True only if exactly one diff at end.

    Complexity:
        Time: O(26 * L) per search where L is word length
        Space: O(N * L) for the trie where N is number of words
    """

    def __init__(self) -> None:
        self.trie = Trie()

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)
