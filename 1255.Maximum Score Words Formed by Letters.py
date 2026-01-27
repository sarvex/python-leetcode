from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        """Find maximum score from valid word subsets using bitmask enumeration.

        Intuition:
            With a small number of words, we can enumerate all possible subsets
            using bitmasks. For each subset, check if the available letters
            suffice and compute the total score.

        Approach:
            Count available letters. Enumerate all 2^n subsets of words. For each
            subset, compute the combined letter frequency and verify it fits within
            the available letters. Track the maximum score among valid subsets.

        Complexity:
            Time: O(2^n * n * L) — n words, L average word length
            Space: O(26) — constant space for letter counters
        """
        available = Counter(letters)
        num_words = len(words)
        max_score = 0
        for mask in range(1 << num_words):
            selected = "".join(words[j] for j in range(num_words) if mask >> j & 1)
            needed = Counter(selected)
            if all(count <= available[char] for char, count in needed.items()):
                total = sum(
                    count * score[ord(char) - ord("a")]
                    for char, count in needed.items()
                )
                max_score = max(max_score, total)
        return max_score
