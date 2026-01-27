from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """Sort by frequency descending then alphabetically for top-k words.

        Intuition:
            Count word frequencies, then sort by frequency (descending) and
            alphabetical order (ascending) to get the top k words.

        Approach:
            1. Count frequencies using Counter.
            2. Sort words by (-frequency, word) to get descending frequency
               with alphabetical tiebreaker.
            3. Return the first k words.

        Complexity:
            Time: O(n log n) for sorting where n is the number of unique words
            Space: O(n) for the frequency counter
        """
        frequency = Counter(words)
        return sorted(frequency, key=lambda word: (-frequency[word], word))[:k]
