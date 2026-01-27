class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 26
        self.is_end: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            index = ord(char) - ord("a")
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        """Trie-based DFS to find words composed of shorter words.

        Intuition:
            Sort words by length and build a trie incrementally. For each
            word, check if it can be decomposed into existing trie words
            before inserting it.

        Approach:
            Sort words by length. For each word, use DFS on the trie to see
            if it can be formed by concatenating previously seen words. If
            not, insert it into the trie for future lookups.

        Complexity:
            Time: O(n * L^2) where n is number of words, L is max word length
            Space: O(n * L) for the trie
        """

        def dfs(word: str) -> bool:
            if not word:
                return True
            node = trie
            for i, char in enumerate(word):
                index = ord(char) - ord("a")
                if node.children[index] is None:
                    return False
                node = node.children[index]
                if node.is_end and dfs(word[i + 1 :]):
                    return True
            return False

        trie = Trie()
        result: list[str] = []
        words.sort(key=lambda x: len(x))
        for word in words:
            if dfs(word):
                result.append(word)
            else:
                trie.insert(word)
        return result
