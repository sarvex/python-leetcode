from collections import Counter


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """Count triplets by precomputing pairwise AND frequencies.

        Intuition:
        Computing all triples directly is O(n^3). By first counting frequencies
        of all pairwise ANDs, we reduce to O(n^2 + n * max_val) by checking
        each pairwise result against each third number.

        Approach:
        1. Compute AND of every pair and count frequencies
        2. For each pairwise AND result and each number in nums
        3. Count combinations where triple AND equals zero

        Complexity:
        Time: O(n^2 + n * max_val) where max_val is the range of AND values
        Space: O(max_val) for the pairwise AND counter
        """
        pairwise_and_count = Counter(x & y for x in nums for y in nums)
        return sum(
            count
            for pair_and, count in pairwise_and_count.items()
            for z in nums
            if pair_and & z == 0
        )
