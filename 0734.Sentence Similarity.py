class Solution:
    def areSentencesSimilar(
        self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]
    ) -> bool:
        """Check sentence similarity using a set of similar word pairs.

        Intuition:
            Two sentences are similar if they have equal length and each word
            pair is either identical or listed in the similar pairs.

        Approach:
            1. Return False immediately if lengths differ.
            2. Build a set of similar pairs for O(1) lookup.
            3. Check each corresponding word pair is equal or in the set
               (checking both orderings).

        Complexity:
            Time: O(n + p) where n is sentence length, p is number of pairs
            Space: O(p) for the similarity set
        """
        if len(sentence1) != len(sentence2):
            return False
        pair_set = {(word_a, word_b) for word_a, word_b in similarPairs}
        return all(
            word1 == word2 or (word1, word2) in pair_set or (word2, word1) in pair_set
            for word1, word2 in zip(sentence1, sentence2)
        )
