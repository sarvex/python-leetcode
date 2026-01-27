from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        """Counter comparison to find the shortest word completing the license plate.

        Intuition:
            Count the letters in the license plate and find the shortest word
            whose letter counts cover all required characters.

        Approach:
            1. Build a frequency counter from the plate's alphabetic characters.
            2. Iterate through words; skip any longer than the current best.
            3. Check that the word's counter covers every plate character.

        Complexity:
            Time: O(N * L) where N = number of words, L = max word length
            Space: O(1) — counters bounded by 26 letters
        """
        plate_count = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        result: str | None = None
        for word in words:
            if result and len(word) >= len(result):
                continue
            word_count = Counter(word)
            if all(count <= word_count[ch] for ch, count in plate_count.items()):
                result = word
        return result
