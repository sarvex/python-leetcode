from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Three-pointer approach from the end to avoid overwriting elements

        Intuition:
        Since nums1 has enough space to hold all elements, we can start filling
        from the end to avoid overwriting elements that we still need to compare.

        Approach:
        1. Use three pointers: p1 (end of nums1 valid elements), p2 (end of nums2),
           and p_merge (end of the merged array)
        2. Compare elements from the end of both arrays and place the larger one
           at the end of nums1
        3. Continue until we've processed all elements from nums2
        4. No need to process remaining nums1 elements as they're already in place

        Complexity:
        Time: O(m + n) - we process each element at most once
        Space: O(1) - we modify nums1 in-place with constant extra space
        """
        first = m - 1  # Index for last element in nums1
        second = n - 1  # Index for last element in nums2
        insert = m + n - 1  # Index for insertion position in merged array

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[insert] = nums1[first]
                first -= 1
            else:
                nums1[insert] = nums2[second]
                second -= 1
            insert -= 1
