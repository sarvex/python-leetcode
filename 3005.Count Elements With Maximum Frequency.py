from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """Tagline: Count total occurrences of elements with the maximum frequency

        Intuition:
        Count frequencies of all numbers, find the highest frequency, then sum
        the counts of all numbers that occur that many times.

        Approach:
        - Build a frequency map using Counter.
        - Compute the maximum frequency.
        - Sum all frequencies equal to the maximum frequency.
        The sum equals max_frequency * number_of_values_at_max_frequency.

        Complexity:
        Time: O(n) where n is len(nums)
        Space: O(k) where k is the number of distinct elements
        """
        if not nums:
            return 0
        counts = Counter(nums)
        max_freq = max(counts.values())
        return sum(freq for freq in counts.values() if freq == max_freq)
