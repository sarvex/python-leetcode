from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Binary search on the product value to find the kth smallest product.

        Intuition:
        Instead of computing all products and sorting them (which would be O(m*n*log(m*n))),
        we can binary search on the possible product values. For each potential product value p,
        we count how many products are less than or equal to p.

        Approach:
        1. Define a helper function 'count(p)' that returns the number of products <= p
        2. For each element x in nums1:
           - If x > 0: Count products x*y <= p using binary search on nums2
           - If x < 0: Count products x*y <= p by finding elements y where x*y > p
           - If x = 0: All products are 0, count them based on sign of p
        3. Binary search on the range [-mx, mx] where mx is the maximum possible absolute product
        4. Return the smallest value p where count(p) >= k

        Complexity:
        Time: O((m+n) * log(max_val^2)) where m, n are lengths of nums1, nums2
        Space: O(1) excluding input
        """
        def count(p: int) -> int:
            """Count the number of products <= p."""
            total = 0
            n = len(nums2)

            for x in nums1:
                if x > 0:
                    # For positive x, find how many y in nums2 satisfy x*y <= p
                    total += bisect_right(nums2, p / x)
                elif x < 0:
                    # For negative x, find how many y in nums2 satisfy x*y <= p
                    # This means y >= p/x since x is negative
                    total += n - bisect_left(nums2, p / x)
                else:
                    # When x = 0, all products are 0
                    # Include all if p >= 0, none if p < 0
                    total += n * int(p >= 0)
            return total

        # Calculate maximum possible absolute product
        max_abs_val1 = max(abs(nums1[0]), abs(nums1[-1])) if nums1 else 0
        max_abs_val2 = max(abs(nums2[0]), abs(nums2[-1])) if nums2 else 0
        mx = max_abs_val1 * max_abs_val2

        # Binary search on the range [-mx, mx]
        return bisect_left(range(-mx, mx + 1), k, key=count) - mx
