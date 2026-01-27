class Solution:
    def removeVowels(self, s: str) -> str:
        """Remove all vowels from the input string.

        Intuition:
            Filter out characters that are vowels while preserving order.

        Approach:
            Use a generator expression to iterate through each character and
            keep only those not in the vowel set.

        Complexity:
            Time: O(n) where n is the length of s
            Space: O(n) for the resulting string
        """
        return "".join(char for char in s if char not in "aeiou")
