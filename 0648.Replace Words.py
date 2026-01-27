class Trie:
    def __init__(self) -> None:
        self.children: list["Trie | None"] = [None] * 26
        self.ref: int = -1

    def insert(self, word: str, index: int) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = index

    def search(self, word: str) -> int:
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                return -1
            node = node.children[idx]
            if node.ref != -1:
                return node.ref
        return -1


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        """Trie-based root replacement finding shortest matching prefix.

        Intuition:
        Build a trie from dictionary roots. For each word in the sentence, search
        the trie for the shortest matching prefix to replace it.

        Approach:
        1. Insert all dictionary roots into a trie, storing their index.
        2. For each word in the sentence, search for the shortest prefix in the trie.
        3. If found, replace the word with the root; otherwise keep the original.

        Complexity:
        Time: O(D + S) where D is total dictionary chars, S is total sentence chars
        Space: O(D)
        """
        trie = Trie()
        for i, word in enumerate(dictionary):
            trie.insert(word, i)
        result = []
        for word in sentence.split():
            idx = trie.search(word)
            result.append(dictionary[idx] if idx != -1 else word)
        return " ".join(result)
