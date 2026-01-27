class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Bijective mapping between pattern characters and words.

        Intuition:
            Each pattern character must map to exactly one word and vice versa.
            Two dictionaries maintain both directions of the mapping.

        Approach:
            1. Split the string into words and check length matches pattern.
            2. Iterate through pattern chars and words simultaneously.
            3. If a char already maps to a different word, or a word already maps
               to a different char, return False.
            4. Otherwise, record both mappings and return True at the end.

        Complexity:
            Time: O(n) where n is the number of words
            Space: O(n)
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}
        for char, word in zip(pattern, words):
            if (char in char_to_word and char_to_word[char] != word) or (
                word in word_to_char and word_to_char[word] != char
            ):
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True
