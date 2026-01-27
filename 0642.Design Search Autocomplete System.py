class Trie:
    def __init__(self) -> None:
        self.children: list["Trie | None"] = [None] * 27
        self.times: int = 0
        self.sentence: str = ""

    def insert(self, word: str, count: int) -> None:
        node = self
        for char in word:
            idx = 26 if char == " " else ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.times += count
        node.sentence = word

    def search(self, prefix: str) -> "Trie | None":
        node = self
        for char in prefix:
            idx = 26 if char == " " else ord(char) - ord("a")
            if node.children[idx] is None:
                return None
            node = node.children[idx]
        return node


class AutocompleteSystem:
    """Trie-based autocomplete system with frequency ranking.

    Intuition:
    Store sentences in a trie with frequency counts. On each character input,
    traverse the trie to find matching completions and rank by frequency.

    Approach:
    1. Build a trie from initial sentences with their frequencies.
    2. On each input character, extend the current prefix and search the trie.
    3. Use DFS to collect all sentences under the matching prefix node.
    4. Sort results by frequency (descending) then lexicographically.
    5. On '#', insert the completed sentence and reset.

    Complexity:
    Time: O(L + S log S) per input where L is trie depth, S is matching sentences
    Space: O(T) where T is total characters across all sentences
    """

    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self.trie = Trie()
        for sentence, count in zip(sentences, times):
            self.trie.insert(sentence, count)
        self.current_input: list[str] = []

    def input(self, c: str) -> list[str]:
        def dfs(node: Trie | None) -> None:
            if node is None:
                return
            if node.times:
                candidates.append((node.times, node.sentence))
            for child in node.children:
                dfs(child)

        if c == "#":
            completed = "".join(self.current_input)
            self.trie.insert(completed, 1)
            self.current_input = []
            return []

        candidates: list[tuple[int, str]] = []
        self.current_input.append(c)
        node = self.trie.search("".join(self.current_input))
        if node is None:
            return candidates
        dfs(node)
        candidates.sort(key=lambda x: (-x[0], x[1]))
        return [sentence for _, sentence in candidates[:3]]
