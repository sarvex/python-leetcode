class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        """Single-pass shortest distance handling identical word pairs.

        Intuition:
            Similar to basic shortest distance, but word1 and word2 may be
            the same. When identical, track consecutive occurrences instead.

        Approach:
            If word1 equals word2, scan for consecutive occurrences and track
            the minimum gap. Otherwise, use the standard two-index approach
            tracking the latest position of each word.

        Complexity:
            Time: O(n) where n is the length of wordsDict
            Space: O(1)
        """
        shortest = len(wordsDict)
        if word1 == word2:
            prev_index = -1
            for i, word in enumerate(wordsDict):
                if word == word1:
                    if prev_index != -1:
                        shortest = min(shortest, i - prev_index)
                    prev_index = i
        else:
            index1 = index2 = -1
            for k, word in enumerate(wordsDict):
                if word == word1:
                    index1 = k
                if word == word2:
                    index2 = k
                if index1 != -1 and index2 != -1:
                    shortest = min(shortest, abs(index1 - index2))
        return shortest
