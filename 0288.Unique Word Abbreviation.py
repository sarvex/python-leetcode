from collections import defaultdict


class ValidWordAbbr:
    """Checks word uniqueness based on abbreviation in a dictionary.

    Intuition:
        An abbreviation collapses a word to its first letter, middle length,
        and last letter. A word is unique if no other dictionary word shares
        its abbreviation.

    Approach:
        Build a mapping from each abbreviation to the set of dictionary words
        that produce it. To check uniqueness, verify that the abbreviation
        either does not exist in the map or every word mapped to it is the
        query word itself.

    Complexity:
        Time: O(n) for initialization, O(k) per isUnique where k is the
              number of words sharing the abbreviation
        Space: O(n) for the abbreviation map
    """

    def __init__(self, dictionary: list[str]) -> None:
        """Initialize with a list of dictionary words, grouped by abbreviation."""
        self.abbreviation_map: dict[str, set[str]] = defaultdict(set)
        for word in dictionary:
            self.abbreviation_map[self._abbreviate(word)].add(word)

    def isUnique(self, word: str) -> bool:
        """Return True if no other word in the dictionary has the same abbreviation."""
        abbr = self._abbreviate(word)
        return abbr not in self.abbreviation_map or all(
            word == entry for entry in self.abbreviation_map[abbr]
        )

    def _abbreviate(self, word: str) -> str:
        """Return the abbreviation of a word."""
        return word if len(word) < 3 else word[0] + str(len(word) - 2) + word[-1]
