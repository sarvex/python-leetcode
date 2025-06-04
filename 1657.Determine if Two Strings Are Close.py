from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """Two strings are considered close if they can be transformed into each other through operations.

        Intuition:
        Two strings are close if they have the same character set and the same frequency distribution
        (regardless of which character has which frequency).

        Approach:
        1. Check if both strings have the same set of characters
        2. Check if the frequency distribution (sorted counts) is the same

        Complexity:
        Time: O(n log n) where n is the length of the strings due to sorting
        Space: O(k) where k is the size of the alphabet (constant for lowercase English letters)
        """
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        counter1, counter2 = Counter(word1), Counter(word2)

        return sorted(counter1.values()) == sorted(counter2.values())
