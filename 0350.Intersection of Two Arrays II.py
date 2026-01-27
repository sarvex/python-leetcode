from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Counter-based intersection preserving duplicates.

        Intuition:
            Count element frequencies in one array, then iterate the other
            array and collect elements while decrementing available counts.

        Approach:
            1. Build a frequency counter from nums1.
            2. For each element in nums2, if the count is positive, include
               it in the result and decrement the count.

        Complexity:
            Time: O(n + m) where n and m are the lengths of the arrays
            Space: O(min(n, m)) for the counter
        """
        frequency = Counter(nums1)
        result: list[int] = []
        for num in nums2:
            if frequency[num]:
                result.append(num)
                frequency[num] -= 1
        return result
