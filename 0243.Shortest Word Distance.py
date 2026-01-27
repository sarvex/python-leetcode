from math import inf


class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        """Single-pass tracking of last seen positions for two words.

        Intuition:
            Track the most recent index of each word as we scan the list.
            Whenever both words have been seen, update the minimum distance.

        Approach:
            Iterate through the word list, recording the latest index for
            word1 and word2. After each update, if both indices are valid,
            compute the absolute difference and track the minimum.

        Complexity:
            Time: O(n) where n is the length of wordsDict
            Space: O(1)
        """
        index1 = index2 = -1
        shortest = inf
        for k, word in enumerate(wordsDict):
            if word == word1:
                index1 = k
            if word == word2:
                index2 = k
            if index1 != -1 and index2 != -1:
                shortest = min(shortest, abs(index1 - index2))
        return shortest
