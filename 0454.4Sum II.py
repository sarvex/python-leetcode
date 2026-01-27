from collections import Counter


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        """Hash map to count complementary pairs from two groups of two arrays.

        Intuition:
            Split the four arrays into two groups. Count all pairwise sums from
            the first group, then for each pairwise sum from the second group,
            look up its negation in the counter.

        Approach:
            1. Compute all pairwise sums of nums1 and nums2, storing counts.
            2. For each pairwise sum of nums3 and nums4, add the count of
               its negation from the counter.

        Complexity:
            Time: O(n^2) for the two nested loops.
            Space: O(n^2) for the counter of pairwise sums.
        """
        pair_sums = Counter(a + b for a in nums1 for b in nums2)
        return sum(pair_sums[-(c + d)] for c in nums3 for d in nums4)
