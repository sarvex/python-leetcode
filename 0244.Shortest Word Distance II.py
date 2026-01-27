from collections import defaultdict
from math import inf


class WordDistance:
    """Precomputed index lookup for repeated shortest word distance queries.

    Stores the positions of each word in a dictionary for efficient
    two-pointer distance computation on repeated queries.
    """

    def __init__(self, wordsDict: list[str]) -> None:
        """Initialize with word positions indexed by word.

        Args:
            wordsDict: List of words to index.
        """
        self.word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        """Find shortest distance between two words using two pointers.

        Intuition:
            Since indices are sorted, a two-pointer merge finds the minimum
            distance in linear time relative to occurrence count.

        Approach:
            Retrieve sorted index lists for both words. Use two pointers
            advancing the smaller index each step, tracking minimum distance.

        Complexity:
            Time: O(m + n) where m, n are occurrence counts
            Space: O(1) extra beyond stored indices
        """
        positions1, positions2 = self.word_indices[word1], self.word_indices[word2]
        min_distance = inf
        i = j = 0
        while i < len(positions1) and j < len(positions2):
            min_distance = min(min_distance, abs(positions1[i] - positions2[j]))
            if positions1[i] <= positions2[j]:
                i += 1
            else:
                j += 1
        return min_distance
