class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """Find 1-indexed position of first word with given prefix.

        Intuition:
            Split the sentence and check each word for the prefix match.

        Approach:
            Iterate through words with 1-based indexing. Return the index
            of the first word that starts with searchWord, or -1 if none.

        Complexity:
            Time: O(n) where n is the sentence length
            Space: O(n) for splitting the sentence
        """
        for index, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return index
        return -1
