class Solution:
    def longestWord(self, words: list[str]) -> str:
        """Find longest word buildable one character at a time from dictionary.

        Intuition:
            A word is buildable if every prefix of it (except empty string)
            is also in the dictionary. Use a set for O(1) prefix lookups.

        Approach:
            1. Store all words in a set.
            2. For each word, check that all prefixes exist in the set.
            3. Track the longest valid word, preferring lexicographically
               smaller ones on ties.

        Complexity:
            Time: O(n * L) where n is number of words, L is max word length
            Space: O(n * L) for the word set
        """
        max_length, result = 0, ""
        word_set = set(words)
        for word in word_set:
            length = len(word)
            if all(word[:i] in word_set for i in range(1, length)):
                if max_length < length:
                    max_length, result = length, word
                elif max_length == length and word < result:
                    result = word
        return result
