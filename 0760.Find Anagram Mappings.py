from collections import defaultdict


class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Index mapping from nums1 to nums2 using a value-to-indices dictionary.

        Intuition:
            For each element in nums1, find any valid index in nums2 with the
            same value. A set of indices per value allows O(1) lookup and removal.

        Approach:
            1. Build a dictionary mapping each value in nums2 to its set of indices.
            2. For each element in nums1, pop an index from the corresponding set.

        Complexity:
            Time: O(N)
            Space: O(N)
        """
        index_map: defaultdict[int, set[int]] = defaultdict(set)
        for i, num in enumerate(nums2):
            index_map[num].add(i)
        return [index_map[num].pop() for num in nums1]
