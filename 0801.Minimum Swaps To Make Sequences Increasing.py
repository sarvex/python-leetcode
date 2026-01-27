class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        """DP tracking minimum swaps with keep/swap states.

        Intuition:
            At each position, we either keep both elements or swap them.
            Track the minimum swaps for both states and transition based on
            whether the sequences remain strictly increasing.

        Approach:
            1. Track two states: no_swap (keep current position) and swap (swap it).
            2. If adjacent elements force a swap relationship, update accordingly.
            3. If cross-comparisons also allow options, take the minimum.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        no_swap, swap = 0, 1
        for i in range(1, len(nums1)):
            prev_no_swap, prev_swap = no_swap, swap
            if nums1[i - 1] >= nums1[i] or nums2[i - 1] >= nums2[i]:
                no_swap, swap = prev_swap, prev_no_swap + 1
            else:
                swap = prev_swap + 1
                if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                    no_swap, swap = min(no_swap, prev_swap), min(swap, prev_no_swap + 1)
        return min(no_swap, swap)
