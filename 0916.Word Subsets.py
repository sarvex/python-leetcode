from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """Max frequency merge of words2 to filter universal words in words1.

        Intuition:
            A word in words1 is universal if it contains all characters with
            at least the maximum frequency required by any word in words2.
            We can merge all words2 requirements into a single frequency map.

        Approach:
            1. Build a combined frequency map from words2 by taking the
               max count for each character across all words.
            2. For each word in words1, check if its character frequencies
               satisfy all requirements in the combined map.
            3. Collect and return all universal words.

        Complexity:
            Time: O(m * k + n * k) where m, n are lengths of words1/words2 and k is max word length
            Space: O(26) for frequency maps
        """
        max_freq: Counter[str] = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, count in word_freq.items():
                max_freq[char] = max(max_freq[char], count)
        result: list[str] = []
        for word in words1:
            word_freq = Counter(word)
            if all(count <= word_freq[char] for char, count in max_freq.items()):
                result.append(word)
        return result
