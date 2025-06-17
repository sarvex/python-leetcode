from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Binary search on the maximum difference to find the minimum possible value.

        Intuition:
        If we can form p pairs with a maximum difference of x, we can also form p pairs
        with any maximum difference greater than x. This monotonicity allows us to use
        binary search to find the minimum valid maximum difference.

        Approach:
        1. Sort the array to ensure adjacent elements have the smallest differences
        2. Define a helper function to check if we can form p pairs with a given max difference
        3. Use binary search to find the smallest difference that allows p pairs
        4. For each potential difference, greedily form pairs by taking adjacent elements

        Complexity:
        Time: O(n log n) where n is the length of nums (sorting + binary search)
        Space: O(1) auxiliary space (not counting the input array)
        """
        def can_form_pairs(max_diff: int) -> bool:
            """Check if we can form p pairs with maximum difference of max_diff."""
            pairs_count = 0
            i = 0

            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    pairs_count += 1
                    i += 2  # Skip both elements as they form a pair
                else:
                    i += 1  # Current element can't form a pair, move to next

            return pairs_count >= p

        # Edge case: if p is 0, no pairs needed
        if p == 0:
            return 0

        nums.sort()

        # Binary search for the minimum valid maximum difference
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left
