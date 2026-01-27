class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        """Set of canonical forms from sorted even and odd indexed characters.

        Intuition:
            Two words are special-equivalent if their even-indexed and
            odd-indexed characters are permutations of each other.

        Approach:
            1. For each word, create a canonical key by sorting characters
               at even indices and odd indices separately, then concatenating.
            2. Count the number of distinct canonical keys using a set.

        Complexity:
            Time: O(n * m log m) where n is number of words, m is word length.
            Space: O(n * m)
        """
        canonical_groups = {
            "".join(sorted(word[::2]) + sorted(word[1::2])) for word in words
        }
        return len(canonical_groups)
