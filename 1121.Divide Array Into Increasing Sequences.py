from itertools import groupby


class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        """Check if the array can be divided into subsequences of length >= k.

        Intuition:
            The bottleneck is the most frequently occurring element, since each
            copy must go into a separate subsequence.

        Approach:
            Find the maximum frequency of any element using groupby (array is
            sorted). The array can be divided iff max_freq * k <= len(nums).

        Complexity:
            Time: O(n) where n is the length of nums
            Space: O(1) aside from groupby iterator
        """
        max_frequency = max(len(list(group)) for _, group in groupby(nums))
        return max_frequency * k <= len(nums)
