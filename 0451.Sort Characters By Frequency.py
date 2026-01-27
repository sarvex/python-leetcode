from collections import Counter


class Solution:
    def frequencySort(self, text: str) -> str:
        """Sort characters by descending frequency using a counter.

        Intuition:
            Count each character's occurrences, then build the result by
            repeating each character according to its frequency in descending order.

        Approach:
            1. Count character frequencies with Counter.
            2. Sort items by frequency in descending order.
            3. Build the result by repeating each character by its count.

        Complexity:
            Time: O(n + k log k) where k is the number of distinct characters.
            Space: O(n) for the counter and result string.
        """
        frequency = Counter(text)
        return "".join(
            char * count
            for char, count in sorted(frequency.items(), key=lambda item: -item[1])
        )
