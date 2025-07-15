class Solution:
    def isValid(self, word: str) -> bool:
        """Check if a string is a valid word.

        Intuition: A valid word must contain both vowels and consonants, be at least 3 characters long,
        and contain only alphanumeric characters.

        Approach:
        1. Check if the word length is at least 3 characters
        2. Iterate through each character to verify it's alphanumeric
        3. Track if we've seen at least one vowel and one consonant
        4. Return true only if all conditions are met

        Complexity:
        Time: O(n) where n is the length of the word
        Space: O(1) as we use constant extra space
        """
        if len(word) < 3:
            return False

        vowels = frozenset("aeiouAEIOU")
        has_vowel = has_consonant = False

        for char in word:
            if not char.isalnum():
                return False

            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
