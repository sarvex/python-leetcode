from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Frequency-based greedy approach to make string k-special

        Intuition:
        A string is k-special if the difference between the maximum and minimum
        character frequency is at most k. We need to find the minimum number of
        characters to delete to achieve this property.

        Approach:
        1. Count the frequency of each character in the word
        2. For each possible minimum frequency value (using existing frequencies),
           calculate the total deletions needed:
           - Delete characters with frequency < min_freq
           - Reduce characters with frequency > min_freq + k
        3. Return the minimum number of deletions

        Complexity:
        Time: O(n + m log m), where n is the length of the word and m is the number of unique characters
        Space: O(m), where m is the number of unique characters
        """
        # Count frequency of each character
        freq_counts = Counter(word)
        frequencies = sorted(freq_counts.values())

        # Try each frequency as the potential minimum frequency
        min_deletions = float('inf')
        for i, min_freq in enumerate(frequencies):
            deletions = 0
            for freq in frequencies:
                if freq < min_freq:
                    # Delete all characters with frequency less than min_freq
                    deletions += freq
                elif freq > min_freq + k:
                    # Reduce characters with frequency greater than min_freq + k
                    deletions += freq - (min_freq + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
