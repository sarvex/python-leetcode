class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        """Hash map lookup with palindrome prefix/suffix splitting.

        Intuition:
            For each word, split it at every position. If one part is a
            palindrome, the reverse of the other part might exist in the
            dictionary, forming a valid palindrome pair.

        Approach:
            1. Build a dictionary mapping each word to its index.
            2. For each word, try all split positions. If the suffix is a
               palindrome and the reverse of the prefix exists, add that pair.
            3. Similarly, if the prefix is a palindrome and the reverse of the
               suffix exists, add that pair.

        Complexity:
            Time: O(n * m^2) where n is number of words and m is max word length
            Space: O(n * m) for the dictionary
        """
        word_index = {word: i for i, word in enumerate(words)}
        result: list[list[int]] = []
        for i, word in enumerate(words):
            for split in range(len(word) + 1):
                prefix, suffix = word[:split], word[split:]
                reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]
                if (
                    reversed_prefix in word_index
                    and word_index[reversed_prefix] != i
                    and suffix == reversed_suffix
                ):
                    result.append([i, word_index[reversed_prefix]])
                if (
                    split
                    and reversed_suffix in word_index
                    and word_index[reversed_suffix] != i
                    and prefix == reversed_prefix
                ):
                    result.append([word_index[reversed_suffix], i])
        return result
