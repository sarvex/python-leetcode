from bisect import bisect_right
from collections import Counter
from string import ascii_lowercase


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        """Compare strings by frequency of the smallest character.

        Intuition:
            Define f(s) as the frequency of the lexicographically smallest character
            in s. For each query, count how many words have a strictly greater f value.

        Approach:
            Compute f for every word, sort these values, then use binary search to
            count how many word frequencies exceed each query's frequency.

        Complexity:
            Time: O((n + q) * L + n log n + q log n) where L is average string length
            Space: O(n)
        """

        def frequency_of_smallest(text: str) -> int:
            counts = Counter(text)
            return next(counts[ch] for ch in ascii_lowercase if counts[ch])

        word_count = len(words)
        sorted_frequencies = sorted(frequency_of_smallest(w) for w in words)
        return [
            word_count - bisect_right(sorted_frequencies, frequency_of_smallest(q))
            for q in queries
        ]
