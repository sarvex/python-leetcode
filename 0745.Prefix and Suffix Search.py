class WordFilter:
    """Precomputed prefix-suffix pair lookup for word index queries.

    Intuition:
        For each word, enumerate every possible (prefix, suffix) pair and
        store the word's index. Later words overwrite earlier ones, giving
        the largest index automatically.

    Approach:
        1. For each word, generate all prefix/suffix combinations.
        2. Store each (prefix, suffix) → index in a dictionary.
        3. Query is a simple dictionary lookup.

    Complexity:
        Time: O(N * L^2) for init, O(1) per query
        Space: O(N * L^2)
    """

    def __init__(self, words: list[str]) -> None:
        self.lookup: dict[tuple[str, str], int] = {}
        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                prefix = word[:i]
                for j in range(length + 1):
                    suffix = word[j:]
                    self.lookup[(prefix, suffix)] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)
