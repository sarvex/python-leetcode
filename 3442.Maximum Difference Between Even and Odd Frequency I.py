from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        """Frequency analysis to find maximum difference between odd and even frequencies.

        Intuition:
            The key insight is to separate character frequencies into odd and even groups,
            then find the maximum odd frequency and minimum even frequency for comparison.

        Approach:
            1. Count the frequency of each character using Counter
            2. Iterate through the frequencies and track:
               - Maximum frequency among characters with odd frequency
               - Minimum frequency among characters with even frequency
            3. Return the difference between these two values

        Complexity:
            Time: O(n) where n is the length of the string
            Space: O(k) where k is the number of unique characters in the string
        """
        char_counts = Counter(s)

        max_odd_freq = 0
        min_even_freq = float('inf')

        for freq in char_counts.values():
            if freq % 2:  # Odd frequency
                max_odd_freq = max(max_odd_freq, freq)
            else:  # Even frequency
                min_even_freq = min(min_even_freq, freq)

        return max_odd_freq - min_even_freq
