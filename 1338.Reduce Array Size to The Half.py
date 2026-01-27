from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        """Find minimum set size to remove at least half the array elements.

        Intuition:
            Greedily remove the most frequent elements first to minimize
            the number of distinct values needed.

        Approach:
            Count frequencies, sort by most common, and accumulate until
            the removed count reaches half the array size.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        frequency = Counter(arr)
        removed = set_size = 0
        for _, count in frequency.most_common():
            removed += count
            set_size += 1
            if removed * 2 >= len(arr):
                break
        return set_size
