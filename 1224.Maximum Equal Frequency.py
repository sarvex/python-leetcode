from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        """Maximum equal frequency prefix length.

        Intuition:
            After removing one element, all remaining elements should have equal
            frequency. Track element counts and count-of-counts to check validity.

        Approach:
            Maintain a frequency counter and a counter of frequencies. At each
            position, check if the prefix is valid by testing three conditions:
            all frequencies are 1, one element has frequency 1 more than others,
            or exactly one element has frequency 1 and removing it equalizes.

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(n) for the counters
        """
        frequency: Counter[int] = Counter()
        freq_count: Counter[int] = Counter()
        result = max_freq = 0
        for index, value in enumerate(nums, 1):
            if value in frequency:
                freq_count[frequency[value]] -= 1
            frequency[value] += 1
            max_freq = max(max_freq, frequency[value])
            freq_count[frequency[value]] += 1
            if max_freq == 1:
                result = index
            elif (
                freq_count[max_freq] * max_freq
                + freq_count[max_freq - 1] * (max_freq - 1)
                == index
                and freq_count[max_freq] == 1
            ):
                result = index
            elif freq_count[max_freq] * max_freq + 1 == index and freq_count[1] == 1:
                result = index
        return result
