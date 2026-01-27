class Trie:
    __slots__ = ["children", "count"]

    def __init__(self) -> None:
        self.children: list[Trie | None] = [None] * 26
        self.count = 0

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord("a")
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.count += 1

    def search(self, word: str) -> int:
        node = self
        prefix_len = 0
        for char in word:
            prefix_len += 1
            idx = ord(char) - ord("a")
            node = node.children[idx]
            if node.count == 1:
                return prefix_len
        return len(word)


class Solution:
    def wordsAbbreviation(self, words: list[str]) -> list[str]:
        """Trie-based word abbreviation using shortest unique prefix.

        Intuition:
            Words with the same length and last character can share abbreviation
            conflicts. Use a trie to find the shortest unique prefix for each word.

        Approach:
            Group words by (length, last_char) and build a trie per group.
            For each word, find the shortest prefix that uniquely identifies it.
            Only abbreviate if the abbreviation is shorter than the original.

        Complexity:
            Time: O(n * k) where n is number of words, k is average word length
            Space: O(n * k)
        """
        tries: dict[tuple[int, str], Trie] = {}
        for word in words:
            word_len = len(word)
            if (word_len, word[-1]) not in tries:
                tries[(word_len, word[-1])] = Trie()
            tries[(word_len, word[-1])].insert(word)
        result: list[str] = []
        for word in words:
            prefix_len = tries[(len(word), word[-1])].search(word)
            result.append(
                word
                if prefix_len + 2 >= len(word)
                else word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]
            )
        return result
