from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """Sum lengths of words formable from available characters.

        Intuition:
            A word can be formed if every character in it appears in chars with
            sufficient frequency.

        Approach:
            Count character frequencies in chars. For each word, check if the
            word's character counts are all within the available counts. If so,
            add the word's length to the result.

        Complexity:
            Time: O(n * k) where n is number of words and k is average word length
            Space: O(1) — at most 26 character counts
        """
        available = Counter(chars)
        result = 0
        for word in words:
            word_count = Counter(word)
            if all(available[ch] >= count for ch, count in word_count.items()):
                result += len(word)
        return result
