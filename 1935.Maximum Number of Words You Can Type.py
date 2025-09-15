class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Count words typable given broken letters — set membership filtering.

        Intuition:
        A word becomes untypable if it contains any broken letter. Thus, filter words with no characters from the broken set.

        Approach:
        - Build a set from brokenLetters for O(1) membership checks.
        - Split the text into words on whitespace.
        - For each word, ensure every character is not in the broken set.
        - Count words that pass the check.

        Complexity:
        Time: O(N), where N is the total number of characters in text.
        Space: O(B), for the set of broken letters (B <= alphabet size).
        """
        broken_set: set[str] = set(brokenLetters)
        return sum(1 for word in text.split() if all(ch not in broken_set for ch in word))
