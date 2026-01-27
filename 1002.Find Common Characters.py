from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """Find common characters appearing in all strings including duplicates.

        Intuition:
            The common characters are the intersection of character frequencies
            across all words, taking the minimum count for each character.

        Approach:
            Start with the frequency counter of the first word. For each
            subsequent word, reduce each character count to the minimum of the
            current count and the new word's count. Expand the final counter.

        Complexity:
            Time: O(n * m) where n is the number of words and m is average length
            Space: O(1) since the counter holds at most 26 characters
        """
        common = Counter(words[0])
        for word in words:
            word_count = Counter(word)
            for char in common:
                common[char] = min(common[char], word_count[char])
        result: list[str] = []
        for char, count in common.items():
            result.extend([char] * count)
        return result
