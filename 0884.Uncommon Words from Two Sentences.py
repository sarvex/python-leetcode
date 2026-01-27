from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        """Counter-based filtering for words appearing exactly once overall.

        Intuition:
            A word is uncommon if it appears exactly once across both sentences
            combined.

        Approach:
            1. Split both sentences into words and combine their counters.
            2. Return all words with a total count of exactly one.

        Complexity:
            Time: O(n + m) where n and m are sentence lengths.
            Space: O(n + m)
        """
        word_counts = Counter(s1.split()) + Counter(s2.split())
        return [word for word, count in word_counts.items() if count == 1]
