class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        """Find all index pairs where a word from the list occurs in text.

        Intuition:
            Check every substring of text against the word set.

        Approach:
            Convert words to a set for O(1) lookup. Enumerate all substrings
            and collect matching pairs sorted by start then end index.

        Complexity:
            Time: O(n^2 * L) where n = len(text), L = average word length for hashing
            Space: O(n^2) worst case for result pairs
        """
        word_set = set(words)
        n = len(text)
        return [
            [i, j] for i in range(n) for j in range(i, n) if text[i : j + 1] in word_set
        ]
