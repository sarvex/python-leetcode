from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Counter-based extraction of top k frequent elements.

        Intuition:
            Count occurrences and return the k most common elements directly
            using Python's Counter.most_common method.

        Approach:
            1. Build a frequency counter from the input list.
            2. Use most_common(k) to retrieve the k highest-frequency elements.

        Complexity:
            Time: O(n log k) where n is the length of nums
            Space: O(n) for the counter
        """
        frequency = Counter(nums)
        return [element for element, _ in frequency.most_common(k)]
